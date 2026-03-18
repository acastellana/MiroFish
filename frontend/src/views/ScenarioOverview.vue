<template>
  <div class="scenario-view">
    <!-- Header -->
    <header class="app-header">
      <div class="header-left">
        <div class="brand" @click="router.push('/')">MIROFISH</div>
      </div>
      <div class="header-center">
        <span class="page-label">◈ Scenario Overview</span>
      </div>
      <div class="header-right">
        <button class="icon-btn" @click="router.push(`/agents/${simulationId}`)" title="Explore Agents">
          ◧ Agents
        </button>
        <button class="icon-btn primary" @click="goRun" v-if="!loading">
          {{ runLabel }} →
        </button>
      </div>
    </header>

    <!-- Loading State -->
    <div v-if="loading" class="loading-screen">
      <span class="loading-spinner"></span>
      <span class="loading-text">Loading scenario data...</span>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="error-screen">
      <div class="error-icon">◇</div>
      <div class="error-msg">{{ error }}</div>
      <button class="btn-back" @click="router.push('/')">← Back to Home</button>
    </div>

    <!-- Main Content -->
    <main v-else class="content">

      <!-- Section 1: Scenario Header -->
      <section class="section scenario-header-section">
        <div class="sim-meta-row">
          <span class="sim-id-tag">{{ formatSimId(simulationId) }}</span>
          <span class="status-badge" :class="statusClass">
            <span class="dot">●</span> {{ statusLabel }}
          </span>
          <span class="meta-item">
            <span class="meta-label">Created</span>
            <span class="meta-value">{{ formatDate(simData?.created_at) }}</span>
          </span>
          <span class="meta-item" v-if="simData?.model_name">
            <span class="meta-label">Model</span>
            <span class="meta-value mono">{{ simData.model_name }}</span>
          </span>
          <span class="meta-item">
            <span class="meta-label">Agents</span>
            <span class="meta-value">{{ simData?.profiles_count || simData?.entities_count || '—' }}</span>
          </span>
        </div>
      </section>

      <!-- Section 2: The Question -->
      <section class="section question-section">
        <div class="section-header">
          <span class="section-label">01 / The Question</span>
          <span class="section-sub">What is this simulation testing?</span>
        </div>
        <div class="question-block" v-if="simulationRequirement">
          <div class="question-text">{{ simulationRequirement }}</div>
        </div>
        <div class="empty-block" v-else>
          <span class="empty-icon">◇</span>
          <span>No simulation requirement found</span>
        </div>
      </section>

      <!-- Two-column layout for World Setup + Forcing Functions -->
      <div class="two-col">

        <!-- Section 3: World Setup -->
        <section class="section world-section">
          <div class="section-header">
            <span class="section-label">02 / World Setup</span>
          </div>

          <div class="world-stats">
            <div class="stat-card">
              <div class="stat-value">{{ totalAgents }}</div>
              <div class="stat-label">Total Agents</div>
            </div>
            <div class="stat-card" v-if="platformsEnabled.length">
              <div class="stat-value">{{ platformsEnabled.join(' + ') }}</div>
              <div class="stat-label">Platforms</div>
            </div>
            <div class="stat-card" v-if="simData?.total_rounds">
              <div class="stat-value">{{ simData.total_rounds }}</div>
              <div class="stat-label">Rounds</div>
            </div>
          </div>

          <!-- Entity type breakdown -->
          <div class="entity-breakdown" v-if="entityTypes.length">
            <div class="breakdown-label">Entity Types</div>
            <div class="entity-bars">
              <div
                v-for="et in entityTypes"
                :key="et.type"
                class="entity-bar-row"
              >
                <span class="entity-dot" :style="{ background: getEntityColor(et.type) }"></span>
                <span class="entity-name">{{ et.type }}</span>
                <div class="bar-track">
                  <div
                    class="bar-fill"
                    :style="{
                      width: barWidth(et.count) + '%',
                      background: getEntityColor(et.type)
                    }"
                  ></div>
                </div>
                <span class="entity-count">{{ et.count }}</span>
              </div>
            </div>
          </div>
          <div class="empty-block small" v-else>
            <span>Entity type data not available yet</span>
          </div>
        </section>

        <!-- Section 4: Forcing Functions -->
        <section class="section forcing-section">
          <div class="section-header">
            <span class="section-label">03 / Forcing Functions</span>
            <span class="section-sub">Initial events that kick off the simulation</span>
          </div>

          <div v-if="initialPosts.length" class="posts-list">
            <div
              v-for="(post, i) in initialPosts"
              :key="i"
              class="post-card"
            >
              <div class="post-header">
                <span class="post-num">{{ String(i + 1).padStart(2, '0') }}</span>
                <span class="post-platform" v-if="post.platform">{{ post.platform }}</span>
                <span class="post-author" v-if="post.author || post.user_name">
                  @{{ post.author || post.user_name }}
                </span>
              </div>
              <div class="post-content">{{ post.content || post.text || post.body || JSON.stringify(post) }}</div>
            </div>
          </div>
          <div class="empty-block small" v-else>
            <span class="empty-icon">◇</span>
            <span>No initial posts/events found in config</span>
          </div>
        </section>

      </div><!-- end two-col -->

      <!-- Section 5: Agent Roster Preview -->
      <section class="section roster-section">
        <div class="section-header">
          <span class="section-label">04 / Agent Roster Preview</span>
          <span class="section-sub">{{ previewAgents.length }} agents shown</span>
          <router-link :to="`/agents/${simulationId}`" class="view-all-link">
            View all agents →
          </router-link>
        </div>

        <div v-if="profilesLoading" class="loading-inline">
          <span class="loading-spinner small"></span> Loading profiles...
        </div>
        <div v-else-if="previewAgents.length" class="roster-grid">
          <div
            v-for="agent in previewAgents"
            :key="agent.user_id || agent.user_name"
            class="roster-card"
            :style="{ borderTopColor: getEntityColor(agent.entity_type || '') }"
          >
            <div class="roster-card-top">
              <span class="agent-name">{{ agent.name || agent.user_name }}</span>
              <span
                v-if="agent.entity_type"
                class="type-badge"
                :style="{ background: getEntityColor(agent.entity_type) + '22', color: getEntityColor(agent.entity_type) }"
              >{{ agent.entity_type }}</span>
            </div>
            <div class="agent-bio">{{ truncate(agent.bio || '', 80) }}</div>
          </div>
        </div>
        <div class="empty-block small" v-else>
          <span class="empty-icon">◇</span>
          <span>Agent profiles not generated yet — run the prepare step first</span>
        </div>
      </section>

      <!-- Section 5b: Seed Files (editable, only when not completed/running) -->
      <section
        v-if="simData?.status !== 'completed' && simData?.status !== 'running' && seedFiles.length"
        class="section seed-files-section"
      >
        <div class="section-header">
          <span class="section-label">05 / Seed Files</span>
          <span class="section-sub">{{ seedFiles.length }} file{{ seedFiles.length !== 1 ? 's' : '' }}</span>
          <button class="seed-copy-all-btn" @click="copyAllFiles" :class="{ 'copied': allCopied }">
            {{ allCopied ? 'Copied ✓' : '⎘ Copy All' }}
          </button>
        </div>

        <div v-if="seedFilesLoading" class="loading-inline">
          <span class="loading-spinner small"></span> Loading seed files...
        </div>

        <div v-else class="seed-files-list">
          <div
            v-for="(file, idx) in seedFiles"
            :key="file.filename"
            class="seed-file-card"
          >
            <div class="seed-file-header" @click="toggleFile(idx)">
              <span class="seed-expand-icon">{{ file._expanded ? '▾' : '▸' }}</span>
              <span class="seed-filename">{{ file.filename }}</span>
              <span class="seed-meta">{{ file.size.toLocaleString() }} chars</span>
              <span v-if="file._unsaved" class="seed-unsaved-badge">Unsaved</span>
              <span v-if="file._saved" class="seed-saved-badge">Saved ✓</span>
            </div>

            <div v-if="file._expanded" class="seed-file-body">
              <textarea
                v-model="file._editContent"
                class="seed-textarea"
                :class="{ 'seed-textarea--dirty': file._unsaved }"
                rows="20"
                spellcheck="false"
                @input="onFileInput(idx)"
              ></textarea>
              <div class="seed-file-actions">
                <button
                  class="seed-save-btn"
                  :disabled="file._saving"
                  @click="saveFile(idx)"
                >
                  {{ file._saving ? 'Saving…' : 'Save' }}
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Section 6: Run CTA -->
      <section class="section cta-section">
        <div class="cta-inner">
          <div class="cta-text">
            <div class="cta-title">Ready to run?</div>
            <div class="cta-sub" v-if="simData?.status === 'completed'">
              This simulation has been completed. View the analysis report.
            </div>
            <div class="cta-sub" v-else-if="simData?.status === 'running'">
              Simulation is currently running.
            </div>
            <div class="cta-sub" v-else>
              Launch the simulation to begin agent interactions.
            </div>
          </div>
          <div class="cta-buttons">
            <button class="btn-explore" @click="router.push(`/agents/${simulationId}`)">
              ◧ Explore Agents
            </button>
            <button class="btn-run" @click="goRun">
              {{ runLabel }} →
            </button>
          </div>
        </div>
      </section>

    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getSimulation } from '../api/simulation'
import { getSimulationProfilesRealtime, getSimulationConfig } from '../api/simulation'
import { getProject, getProjectFiles, updateProjectFile } from '../api/graph'

const route = useRoute()
const router = useRouter()
const simulationId = route.params.simulationId

// State
const loading = ref(true)
const profilesLoading = ref(true)
const seedFilesLoading = ref(false)
const error = ref('')
const simData = ref(null)
const projectData = ref(null)
const configData = ref(null)
const profiles = ref([])
const seedFiles = ref([])
const allCopied = ref(false)

// Entity color palette
const ENTITY_COLORS = {
  MarketplaceOperator: '#ff6b35',
  Developer: '#4ecdc4',
  EnterpriseBuyer: '#45b7d1',
  Investor: '#96ceb4',
  FrameworkBuilder: '#feca57',
  Regulator: '#a29bfe',
  Media: '#fd79a8',
  Competitor: '#e17055',
}
const DEFAULT_COLORS = ['#74b9ff', '#a29bfe', '#55efc4', '#fdcb6e', '#e84393', '#00cec9']

const getEntityColor = (type) => {
  if (ENTITY_COLORS[type]) return ENTITY_COLORS[type]
  // Hash-based fallback
  let hash = 0
  for (let i = 0; i < type.length; i++) hash = type.charCodeAt(i) + ((hash << 5) - hash)
  return DEFAULT_COLORS[Math.abs(hash) % DEFAULT_COLORS.length]
}

// Computed
const simulationRequirement = computed(() => {
  return projectData.value?.simulation_requirement || simData.value?.simulation_requirement || ''
})

const totalAgents = computed(() => {
  return simData.value?.profiles_count || simData.value?.entities_count || '—'
})

const platformsEnabled = computed(() => {
  const p = []
  if (simData.value?.enable_reddit !== false) p.push('Reddit')
  if (simData.value?.enable_twitter) p.push('Twitter')
  return p
})

const entityTypes = computed(() => {
  // From simulation entity_types field
  if (simData.value?.entity_types && typeof simData.value.entity_types === 'object') {
    return Object.entries(simData.value.entity_types).map(([type, count]) => ({ type, count }))
  }
  return []
})

const maxEntityCount = computed(() => {
  return Math.max(...entityTypes.value.map(e => e.count), 1)
})

const barWidth = (count) => Math.round((count / maxEntityCount.value) * 100)

const initialPosts = computed(() => {
  if (!configData.value) return []
  const cfg = configData.value

  // Try multiple known keys
  const candidates = cfg.initial_posts || cfg.initial_actions || cfg.seed_posts ||
    cfg.reddit_config?.initial_posts || cfg.twitter_config?.initial_posts || []
  return Array.isArray(candidates) ? candidates.slice(0, 10) : []
})

const previewAgents = computed(() => profiles.value.slice(0, 12))

const statusClass = computed(() => {
  const s = simData.value?.status
  if (s === 'completed') return 'completed'
  if (s === 'running') return 'running'
  if (s === 'error') return 'error'
  return 'idle'
})

const statusLabel = computed(() => {
  const s = simData.value?.status
  if (s === 'completed') return 'Completed'
  if (s === 'running') return 'Running'
  if (s === 'error') return 'Error'
  return 'Ready'
})

const runLabel = computed(() => {
  if (simData.value?.status === 'completed' && simData.value?.report_id) {
    return 'View Report'
  }
  return 'Run Simulation'
})

const goRun = () => {
  if (simData.value?.status === 'completed' && simData.value?.report_id) {
    router.push({ name: 'Report', params: { reportId: simData.value.report_id } })
  } else {
    router.push({ name: 'SimulationRun', params: { simulationId } })
  }
}

// Helpers
const formatSimId = (id) => {
  if (!id) return 'SIM'
  return 'SIM_' + id.replace('sim_', '').slice(0, 6).toUpperCase()
}

const formatDate = (dateStr) => {
  if (!dateStr) return '—'
  try {
    return new Date(dateStr).toISOString().slice(0, 16).replace('T', ' ')
  } catch { return dateStr }
}

const truncate = (str, n) => str.length > n ? str.slice(0, n) + '…' : str

// Data loading
const loadAll = async () => {
  try {
    // Load simulation
    const simRes = await getSimulation(simulationId)
    if (!simRes.success) throw new Error(simRes.error || 'Failed to load simulation')
    simData.value = simRes.data

    // Load project (for simulation_requirement)
    if (simRes.data?.project_id) {
      const projRes = await getProject(simRes.data.project_id)
      if (projRes.success) projectData.value = projRes.data
      // Load seed files (non-blocking, only when editable)
      if (simRes.data.status !== 'completed' && simRes.data.status !== 'running') {
        loadSeedFiles(simRes.data.project_id)
      }
    }

    // Load config (for initial posts / forcing functions)
    try {
      const cfgRes = await getSimulationConfig(simulationId)
      if (cfgRes.success && cfgRes.data) configData.value = cfgRes.data
    } catch (e) {
      // Config may not be ready — non-fatal
    }
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }

  // Load profiles separately (non-blocking)
  loadProfiles()
}

const loadProfiles = async () => {
  profilesLoading.value = true
  try {
    const res = await getSimulationProfilesRealtime(simulationId, 'reddit')
    const profileList = res.data?.profiles ?? res.data
    if (res.success && Array.isArray(profileList)) {
      profiles.value = profileList
    }
  } catch (e) {
    // Profiles not ready — show empty state
  } finally {
    profilesLoading.value = false
  }
}

// Seed Files
const loadSeedFiles = async (projectId) => {
  if (!projectId) return
  seedFilesLoading.value = true
  try {
    const res = await getProjectFiles(projectId)
    if (res.success && res.data?.files) {
      seedFiles.value = res.data.files.map(f => ({
        ...f,
        _editContent: f.content,
        _unsaved: false,
        _saving: false,
        _saved: false,
        _expanded: false,
      }))
    }
  } catch (e) {
    // Non-fatal
  } finally {
    seedFilesLoading.value = false
  }
}

const toggleFile = (idx) => {
  seedFiles.value[idx]._expanded = !seedFiles.value[idx]._expanded
}

const copyAllFiles = async () => {
  const text = seedFiles.value.map(f =>
    `# ${f.filename}\n\n${f._editContent || f.content}`
  ).join('\n\n---\n\n')
  try {
    await navigator.clipboard.writeText(text)
    allCopied.value = true
    setTimeout(() => { allCopied.value = false }, 2000)
  } catch (e) {
    // Fallback for non-https or denied permissions
    const ta = document.createElement('textarea')
    ta.value = text
    document.body.appendChild(ta)
    ta.select()
    document.execCommand('copy')
    document.body.removeChild(ta)
    allCopied.value = true
    setTimeout(() => { allCopied.value = false }, 2000)
  }
}

const onFileInput = (idx) => {
  const f = seedFiles.value[idx]
  f._unsaved = f._editContent !== f.content
  f._saved = false
}

const saveFile = async (idx) => {
  const f = seedFiles.value[idx]
  const projectId = projectData.value?.project_id || simData.value?.project_id
  if (!projectId) return
  f._saving = true
  try {
    const res = await updateProjectFile(projectId, f.filename, f._editContent)
    if (res.success) {
      f.content = f._editContent
      f.size = f._editContent.length
      f._unsaved = false
      f._saved = true
      setTimeout(() => { f._saved = false }, 2000)
    }
  } catch (e) {
    // Show nothing; user can retry
  } finally {
    f._saving = false
  }
}

onMounted(() => { loadAll() })
</script>

<style scoped>
/* ===== Base ===== */
.scenario-view {
  min-height: 100vh;
  background: #fff;
  font-family: 'Space Grotesk', system-ui, sans-serif;
  color: #111;
}

/* ===== Header ===== */
.app-header {
  height: 56px;
  border-bottom: 1px solid #eaeaea;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  background: #fff;
  position: sticky;
  top: 0;
  z-index: 100;
}

.brand {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 800;
  font-size: 16px;
  letter-spacing: 1px;
  cursor: pointer;
}

.page-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: #666;
  letter-spacing: 0.5px;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 10px;
}

.icon-btn {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 600;
  padding: 6px 14px;
  border: 1px solid #e5e5e5;
  background: transparent;
  cursor: pointer;
  color: #555;
  letter-spacing: 0.3px;
  transition: all 0.2s;
}
.icon-btn:hover { border-color: #000; color: #000; }
.icon-btn.primary {
  background: #000;
  color: #fff;
  border-color: #000;
}
.icon-btn.primary:hover { background: #ff4500; border-color: #ff4500; }

/* ===== Loading / Error ===== */
.loading-screen, .error-screen {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  gap: 16px;
  color: #999;
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
}
.error-icon { font-size: 2rem; opacity: 0.4; }
.error-msg { color: #e17055; }
.btn-back {
  margin-top: 8px;
  padding: 8px 20px;
  border: 1px solid #ddd;
  background: transparent;
  cursor: pointer;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  transition: all 0.2s;
}
.btn-back:hover { border-color: #000; }

.loading-spinner {
  width: 24px;
  height: 24px;
  border: 2px solid #eee;
  border-top-color: #555;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  display: inline-block;
}
.loading-spinner.small { width: 16px; height: 16px; }
@keyframes spin { to { transform: rotate(360deg); } }
.loading-inline {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: #999;
  padding: 20px 0;
}

/* ===== Content ===== */
.content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 32px 24px 80px;
}

/* ===== Section base ===== */
.section {
  margin-bottom: 40px;
}

.section-header {
  display: flex;
  align-items: baseline;
  gap: 14px;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid #f0f0f0;
}
.section-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1px;
  color: #888;
  text-transform: uppercase;
}
.section-sub {
  font-size: 12px;
  color: #bbb;
}
.view-all-link {
  margin-left: auto;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: #666;
  text-decoration: none;
  transition: color 0.2s;
}
.view-all-link:hover { color: #000; }

/* ===== Section 1: Scenario header ===== */
.sim-meta-row {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}
.sim-id-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 700;
  background: #f3f4f6;
  padding: 4px 10px;
  letter-spacing: 1px;
}
.status-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 2px;
}
.status-badge .dot { font-size: 8px; }
.status-badge.completed { background: rgba(16,185,129,0.1); color: #059669; }
.status-badge.running { background: rgba(245,158,11,0.1); color: #d97706; }
.status-badge.error { background: rgba(239,68,68,0.1); color: #dc2626; }
.status-badge.idle { background: #f3f4f6; color: #6b7280; }

.meta-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
}
.meta-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: #bbb;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.meta-value { color: #333; font-weight: 500; }
.meta-value.mono { font-family: 'JetBrains Mono', monospace; font-size: 11px; }

/* ===== Section 2: Question ===== */
.question-block {
  background: #f9f9f9;
  border: 1px solid #e8e8e8;
  border-left: 4px solid #ff4500;
  padding: 24px 28px;
}
.question-text {
  font-size: 1.15rem;
  font-weight: 500;
  line-height: 1.7;
  color: #1a1a1a;
}

/* ===== Two-column layout ===== */
.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  margin-bottom: 40px;
}

/* ===== Section 3: World setup ===== */
.world-stats {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}
.stat-card {
  flex: 1;
  min-width: 80px;
  border: 1px solid #e8e8e8;
  padding: 14px 16px;
}
.stat-value {
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.4rem;
  font-weight: 700;
  color: #111;
  margin-bottom: 4px;
}
.stat-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: #aaa;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.entity-breakdown { margin-top: 8px; }
.breakdown-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: #aaa;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 12px;
}
.entity-bars { display: flex; flex-direction: column; gap: 10px; }
.entity-bar-row {
  display: flex;
  align-items: center;
  gap: 10px;
}
.entity-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}
.entity-name {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: #444;
  width: 160px;
  flex-shrink: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.bar-track {
  flex: 1;
  height: 6px;
  background: #f0f0f0;
  border-radius: 3px;
  overflow: hidden;
}
.bar-fill {
  height: 100%;
  border-radius: 3px;
  transition: width 0.6s ease;
}
.entity-count {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: #888;
  min-width: 24px;
  text-align: right;
}

/* ===== Section 4: Forcing Functions ===== */
.posts-list { display: flex; flex-direction: column; gap: 12px; }
.post-card {
  border: 1px solid #e8e8e8;
  padding: 14px 16px;
}
.post-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}
.post-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: #ccc;
  font-weight: 700;
}
.post-platform {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  background: #f3f4f6;
  padding: 2px 6px;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.post-author {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: #888;
}
.post-content {
  font-size: 13px;
  line-height: 1.5;
  color: #333;
}

/* ===== Section 5: Roster ===== */
.roster-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 14px;
}
.roster-card {
  border: 1px solid #e8e8e8;
  border-top-width: 3px;
  padding: 14px;
  transition: box-shadow 0.2s, transform 0.2s;
}
.roster-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  transform: translateY(-2px);
}
.roster-card-top {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 8px;
}
.agent-name {
  font-weight: 700;
  font-size: 14px;
  color: #111;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.type-badge {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.5px;
  padding: 2px 7px;
  border-radius: 2px;
  text-transform: uppercase;
}
.agent-bio {
  font-size: 11px;
  line-height: 1.5;
  color: #777;
}

/* ===== Section 6: CTA ===== */
.cta-section {
  border-top: 2px solid #000;
  padding-top: 32px;
  margin-bottom: 0;
}
.cta-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 24px;
}
.cta-title {
  font-size: 1.4rem;
  font-weight: 700;
  margin-bottom: 6px;
}
.cta-sub {
  font-size: 13px;
  color: #888;
}
.cta-buttons { display: flex; gap: 12px; flex-shrink: 0; }
.btn-explore {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 600;
  padding: 12px 20px;
  border: 1px solid #ddd;
  background: transparent;
  cursor: pointer;
  transition: all 0.2s;
  letter-spacing: 0.3px;
}
.btn-explore:hover { border-color: #000; }
.btn-run {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 600;
  padding: 12px 24px;
  border: none;
  background: #000;
  color: #fff;
  cursor: pointer;
  letter-spacing: 0.3px;
  transition: background 0.2s;
}
.btn-run:hover { background: #ff4500; }

/* ===== Empty Block ===== */
.empty-block {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 32px;
  border: 1px dashed #e0e0e0;
  color: #bbb;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
}
.empty-block.small { padding: 20px; }
.empty-icon { font-size: 1.2rem; opacity: 0.5; }

/* ===== Section 5b: Seed Files ===== */
.seed-files-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.seed-copy-all-btn {
  margin-left: auto;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 600;
  padding: 5px 14px;
  border: 1px solid #ddd;
  background: transparent;
  cursor: pointer;
  color: #555;
  letter-spacing: 0.3px;
  transition: all 0.2s;
}
.seed-copy-all-btn:hover { border-color: #000; color: #000; }
.seed-copy-all-btn.copied { border-color: #059669; color: #059669; }

.seed-file-card {
  border: 1px solid #e8e8e8;
}

.seed-file-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  cursor: pointer;
  user-select: none;
  transition: background 0.15s;
}
.seed-file-header:hover {
  background: #fafafa;
}

.seed-expand-icon {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: #999;
  width: 12px;
  flex-shrink: 0;
}

.seed-filename {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 600;
  color: #222;
  text-transform: lowercase;
  letter-spacing: 0.3px;
  flex: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.seed-meta {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: #bbb;
  flex-shrink: 0;
}

.seed-unsaved-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 700;
  background: rgba(245, 158, 11, 0.12);
  color: #d97706;
  padding: 2px 8px;
  letter-spacing: 0.3px;
  flex-shrink: 0;
}

.seed-saved-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 700;
  background: rgba(16, 185, 129, 0.1);
  color: #059669;
  padding: 2px 8px;
  letter-spacing: 0.3px;
  flex-shrink: 0;
}

.seed-file-body {
  border-top: 1px solid #f0f0f0;
  padding: 16px;
}

.seed-textarea {
  width: 100%;
  box-sizing: border-box;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  line-height: 1.6;
  border: 1px solid #e0e0e0;
  padding: 12px 14px;
  resize: vertical;
  color: #222;
  background: #fafafa;
  transition: border-color 0.2s;
  outline: none;
}
.seed-textarea:focus {
  border-color: #aaa;
  background: #fff;
}
.seed-textarea--dirty {
  border-color: #f59e0b;
  background: #fffbf0;
}

.seed-file-actions {
  margin-top: 10px;
  display: flex;
  justify-content: flex-end;
}

.seed-save-btn {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 700;
  padding: 8px 20px;
  border: none;
  background: #000;
  color: #fff;
  cursor: pointer;
  letter-spacing: 0.5px;
  transition: background 0.2s;
}
.seed-save-btn:hover:not(:disabled) {
  background: #ff4500;
}
.seed-save-btn:disabled {
  background: #bbb;
  cursor: not-allowed;
}

/* ===== Responsive ===== */
@media (max-width: 768px) {
  .two-col { grid-template-columns: 1fr; }
  .cta-inner { flex-direction: column; align-items: flex-start; }
  .header-center { display: none; }
  .sim-meta-row { gap: 10px; }
}
</style>
