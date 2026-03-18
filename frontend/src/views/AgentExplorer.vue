<template>
  <div class="agent-explorer">
    <!-- Header -->
    <header class="app-header">
      <div class="header-left">
        <div class="brand" @click="router.push('/')">MIROFISH</div>
      </div>
      <div class="header-center">
        <span class="page-label">◧ Agent Explorer</span>
      </div>
      <div class="header-right">
        <button class="icon-btn" @click="router.push(`/scenario/${simulationId}`)">
          ◈ Scenario
        </button>
        <button class="icon-btn primary" @click="router.push({ name: 'SimulationRun', params: { simulationId } })">
          Run →
        </button>
      </div>
    </header>

    <!-- Loading State -->
    <div v-if="loading" class="loading-screen">
      <span class="loading-spinner"></span>
      <span class="loading-text">Loading agents...</span>
    </div>

    <main v-else class="content">

      <!-- Stats Bar -->
      <div class="stats-bar">
        <div class="stat-item">
          <span class="stat-value">{{ allAgents.length }}</span>
          <span class="stat-label">Total Agents</span>
        </div>
        <div class="stat-divider"></div>
        <div
          v-for="et in entityTypeCounts"
          :key="et.type"
          class="stat-item"
        >
          <span class="stat-value" :style="{ color: getEntityColor(et.type) }">{{ et.count }}</span>
          <span class="stat-label">{{ et.type }}</span>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-item" v-if="redditCount > 0">
          <span class="stat-value reddit-color">{{ redditCount }}</span>
          <span class="stat-label">Reddit</span>
        </div>
        <div class="stat-item" v-if="twitterCount > 0">
          <span class="stat-value twitter-color">{{ twitterCount }}</span>
          <span class="stat-label">Twitter</span>
        </div>
      </div>

      <!-- Filter Bar -->
      <div class="filter-bar">
        <div class="search-wrapper">
          <span class="search-icon">⌕</span>
          <input
            v-model="searchQuery"
            class="search-input"
            placeholder="Search by name..."
            type="text"
          />
          <button v-if="searchQuery" class="clear-search" @click="searchQuery = ''">×</button>
        </div>

        <div class="type-filters">
          <button
            class="filter-chip"
            :class="{ active: activeTypeFilter === '' }"
            @click="activeTypeFilter = ''"
          >All</button>
          <button
            v-for="et in availableTypes"
            :key="et"
            class="filter-chip"
            :class="{ active: activeTypeFilter === et }"
            :style="activeTypeFilter === et ? { background: getEntityColor(et), borderColor: getEntityColor(et), color: '#fff' } : {}"
            @click="activeTypeFilter = et"
          >
            <span class="chip-dot" :style="{ background: getEntityColor(et) }"></span>
            {{ et }}
          </button>
        </div>

        <div class="filter-meta">
          {{ filteredAgents.length }} of {{ allAgents.length }} agents
        </div>
      </div>

      <!-- Empty States -->
      <div v-if="allAgents.length === 0" class="empty-state">
        <div class="empty-icon">◧</div>
        <div class="empty-title">No agent profiles yet</div>
        <div class="empty-sub">Run the "Prepare" step on the simulation to generate agent profiles.</div>
        <button class="btn-go" @click="router.push({ name: 'Simulation', params: { simulationId } })">
          → Go to Environment Setup
        </button>
      </div>

      <div v-else-if="filteredAgents.length === 0" class="empty-state small">
        <div class="empty-icon">◇</div>
        <div class="empty-sub">No agents match your filter.</div>
        <button class="btn-clear" @click="clearFilters">Clear filters</button>
      </div>

      <!-- Agent Grid -->
      <div v-else class="agents-grid">
        <div
          v-for="agent in filteredAgents"
          :key="agent._key"
          class="agent-card"
          :style="{ borderTopColor: getEntityColor(agent.entity_type || '') }"
          @click="openModal(agent)"
        >
          <div class="agent-card-header">
            <div class="agent-name-row">
              <span class="agent-name">{{ agent.name || agent.user_name }}</span>
              <span class="platform-badge" :class="agent._platform">
                {{ agent._platform === 'reddit' ? '◉ Reddit' : '✦ Twitter' }}
              </span>
            </div>
            <span
              v-if="agent.entity_type"
              class="type-badge"
              :style="{ background: getEntityColor(agent.entity_type) + '22', color: getEntityColor(agent.entity_type) }"
            >{{ agent.entity_type }}</span>
          </div>

          <div class="agent-bio">{{ truncate(agent.bio || '', 120) }}</div>

          <div v-if="extractMotivation(agent)" class="agent-motivation">
            <span class="motivation-label">Motivation</span>
            <span class="motivation-text">{{ truncate(extractMotivation(agent), 100) }}</span>
          </div>

          <div class="agent-card-footer">
            <span class="username-tag">@{{ agent.user_name }}</span>
            <span class="expand-hint">Click to expand →</span>
          </div>
        </div>
      </div>
    </main>

    <!-- Agent Detail Modal -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="selectedAgent" class="modal-overlay" @click.self="closeModal">
          <div class="modal-content">
            <div class="modal-header">
              <div class="modal-title-row">
                <span class="modal-name">{{ selectedAgent.name || selectedAgent.user_name }}</span>
                <span
                  v-if="selectedAgent.entity_type"
                  class="type-badge large"
                  :style="{ background: getEntityColor(selectedAgent.entity_type) + '22', color: getEntityColor(selectedAgent.entity_type) }"
                >{{ selectedAgent.entity_type }}</span>
                <span class="platform-badge" :class="selectedAgent._platform">
                  {{ selectedAgent._platform === 'reddit' ? '◉ Reddit' : '✦ Twitter' }}
                </span>
              </div>
              <span class="modal-username">@{{ selectedAgent.user_name }}</span>
              <button class="modal-close" @click="closeModal">×</button>
            </div>

            <div class="modal-body">
              <div class="modal-section" v-if="selectedAgent.bio">
                <div class="modal-label">Bio / Persona</div>
                <div class="modal-text">{{ selectedAgent.bio }}</div>
              </div>

              <div class="modal-section" v-if="selectedAgent.other_info">
                <div class="modal-label">Background & Goals</div>
                <div class="modal-text other-info">{{ selectedAgent.other_info }}</div>
              </div>

              <div class="modal-section" v-if="selectedAgent.user_id !== undefined">
                <div class="modal-label">Agent ID</div>
                <div class="modal-text mono">{{ selectedAgent.user_id }}</div>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getSimulationProfilesRealtime, getSimulation } from '../api/simulation'

const route = useRoute()
const router = useRouter()
const simulationId = route.params.simulationId

// State
const loading = ref(true)
const allAgents = ref([])
const searchQuery = ref('')
const activeTypeFilter = ref('')
const selectedAgent = ref(null)

// Entity color palette (consistent with ScenarioOverview)
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
  if (!type) return '#aaa'
  if (ENTITY_COLORS[type]) return ENTITY_COLORS[type]
  let hash = 0
  for (let i = 0; i < type.length; i++) hash = type.charCodeAt(i) + ((hash << 5) - hash)
  return DEFAULT_COLORS[Math.abs(hash) % DEFAULT_COLORS.length]
}

// Computed
const availableTypes = computed(() => {
  const types = new Set(allAgents.value.map(a => a.entity_type).filter(Boolean))
  return Array.from(types).sort()
})

const entityTypeCounts = computed(() => {
  const counts = {}
  allAgents.value.forEach(a => {
    if (a.entity_type) counts[a.entity_type] = (counts[a.entity_type] || 0) + 1
  })
  return Object.entries(counts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 6)
    .map(([type, count]) => ({ type, count }))
})

const redditCount = computed(() => allAgents.value.filter(a => a._platform === 'reddit').length)
const twitterCount = computed(() => allAgents.value.filter(a => a._platform === 'twitter').length)

const filteredAgents = computed(() => {
  let agents = allAgents.value

  if (activeTypeFilter.value) {
    agents = agents.filter(a => a.entity_type === activeTypeFilter.value)
  }

  if (searchQuery.value.trim()) {
    const q = searchQuery.value.toLowerCase()
    agents = agents.filter(a =>
      (a.name || '').toLowerCase().includes(q) ||
      (a.user_name || '').toLowerCase().includes(q)
    )
  }

  return agents
})

// Helpers
const truncate = (str, n) => {
  if (!str) return ''
  return str.length > n ? str.slice(0, n) + '…' : str
}

const extractMotivation = (agent) => {
  if (!agent.other_info) return ''
  // Try to find "Motivations:" line in other_info
  const match = agent.other_info.match(/Motivations?:\s*(.+?)(?:\n|$)/i)
  return match ? match[1].trim() : ''
}

const clearFilters = () => {
  searchQuery.value = ''
  activeTypeFilter.value = ''
}

const openModal = (agent) => { selectedAgent.value = agent }
const closeModal = () => { selectedAgent.value = null }

// Data loading
const mergeProfiles = (profiles, platform) => {
  return profiles.map(p => ({
    ...p,
    _platform: platform,
    _key: `${platform}-${p.user_id || p.user_name}`,
  }))
}

const loadProfiles = async () => {
  loading.value = true
  try {
    // Load both platforms in parallel
    const [redditRes, twitterRes] = await Promise.allSettled([
      getSimulationProfilesRealtime(simulationId, 'reddit'),
      getSimulationProfilesRealtime(simulationId, 'twitter'),
    ])

    let combined = []

    if (redditRes.status === 'fulfilled' && redditRes.value?.success) {
      const rProfiles = redditRes.value.data?.profiles ?? redditRes.value.data
      if (Array.isArray(rProfiles)) combined.push(...mergeProfiles(rProfiles, 'reddit'))
    }
    if (twitterRes.status === 'fulfilled' && twitterRes.value?.success) {
      const tProfiles = twitterRes.value.data?.profiles ?? twitterRes.value.data
      if (Array.isArray(tProfiles)) combined.push(...mergeProfiles(tProfiles, 'twitter'))
    }

    // Deduplicate by user_name (keep reddit version if duplicate)
    const seen = new Set()
    allAgents.value = combined.filter(a => {
      const key = (a.user_name || a.name || '').toLowerCase()
      if (seen.has(key)) return false
      seen.add(key)
      return true
    })

    // Also try to enrich entity_type from simulation data if profiles lack it
    if (allAgents.value.length > 0 && !allAgents.value[0].entity_type) {
      await enrichEntityTypes()
    }
  } catch (e) {
    console.warn('Error loading profiles:', e)
  } finally {
    loading.value = false
  }
}

const enrichEntityTypes = async () => {
  try {
    const simRes = await getSimulation(simulationId)
    if (!simRes.success || !simRes.data?.entity_types) return
    const entityTypes = simRes.data.entity_types

    // entity_types may be an object like { MarketplaceOperator: 5, Developer: 3 }
    // We can't reliably map individual agents without explicit field in profile
    // Try to extract from bio/other_info using keyword matching
    const typeKeys = Object.keys(entityTypes)
    allAgents.value = allAgents.value.map(agent => {
      if (agent.entity_type) return agent
      // Check bio and other_info for type keywords
      const text = `${agent.bio || ''} ${agent.other_info || ''}`.toLowerCase()
      const matched = typeKeys.find(t => text.includes(t.toLowerCase()))
      return { ...agent, entity_type: matched || '' }
    })
  } catch (e) {
    // non-fatal
  }
}

onMounted(() => { loadProfiles() })
</script>

<style scoped>
/* ===== Base ===== */
.agent-explorer {
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
.header-right { display: flex; align-items: center; gap: 10px; }

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
.icon-btn.primary { background: #000; color: #fff; border-color: #000; }
.icon-btn.primary:hover { background: #ff4500; border-color: #ff4500; }

/* ===== Loading ===== */
.loading-screen {
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
.loading-spinner {
  width: 24px;
  height: 24px;
  border: 2px solid #eee;
  border-top-color: #555;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  display: inline-block;
}
@keyframes spin { to { transform: rotate(360deg); } }

/* ===== Content ===== */
.content {
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 24px 80px;
}

/* ===== Stats Bar ===== */
.stats-bar {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 16px 0;
  border-bottom: 1px solid #f0f0f0;
  flex-wrap: wrap;
  overflow-x: auto;
}
.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  min-width: 60px;
}
.stat-value {
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.1rem;
  font-weight: 700;
  color: #111;
  line-height: 1;
}
.stat-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px;
  color: #bbb;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  text-align: center;
}
.stat-divider {
  width: 1px;
  height: 32px;
  background: #eee;
}
.reddit-color { color: #ff4500 !important; }
.twitter-color { color: #1da1f2 !important; }

/* ===== Filter Bar ===== */
.filter-bar {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px 0;
  flex-wrap: wrap;
  border-bottom: 1px solid #f0f0f0;
  margin-bottom: 24px;
}
.search-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  flex-shrink: 0;
}
.search-icon {
  position: absolute;
  left: 10px;
  color: #bbb;
  font-size: 16px;
  pointer-events: none;
}
.search-input {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  padding: 8px 32px 8px 32px;
  border: 1px solid #ddd;
  background: #fafafa;
  outline: none;
  width: 200px;
  color: #111;
  transition: border-color 0.2s;
}
.search-input:focus { border-color: #666; background: #fff; }
.clear-search {
  position: absolute;
  right: 8px;
  background: none;
  border: none;
  cursor: pointer;
  color: #aaa;
  font-size: 16px;
  line-height: 1;
  padding: 0;
}
.clear-search:hover { color: #333; }

.type-filters {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}
.filter-chip {
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 600;
  padding: 5px 12px;
  border: 1px solid #ddd;
  background: transparent;
  cursor: pointer;
  color: #555;
  letter-spacing: 0.3px;
  transition: all 0.2s;
  text-transform: uppercase;
}
.filter-chip:hover { border-color: #999; color: #111; }
.filter-chip.active { border-color: #000; color: #000; background: #f0f0f0; }
.chip-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
}

.filter-meta {
  margin-left: auto;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: #bbb;
  flex-shrink: 0;
}

/* ===== Empty State ===== */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 80px 24px;
  gap: 12px;
  text-align: center;
}
.empty-state.small { padding: 40px 24px; }
.empty-icon { font-size: 2.5rem; opacity: 0.3; }
.empty-title { font-size: 1.2rem; font-weight: 700; }
.empty-sub { font-size: 13px; color: #999; max-width: 400px; line-height: 1.5; }
.btn-go, .btn-clear {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 600;
  padding: 10px 20px;
  border: 1px solid #000;
  background: #000;
  color: #fff;
  cursor: pointer;
  margin-top: 8px;
  transition: background 0.2s;
}
.btn-go:hover, .btn-clear:hover { background: #333; }
.btn-clear { background: transparent; color: #555; border-color: #ddd; }
.btn-clear:hover { background: transparent; border-color: #999; color: #111; }

/* ===== Agent Grid ===== */
.agents-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 16px;
}

.agent-card {
  border: 1px solid #e8e8e8;
  border-top-width: 3px;
  padding: 16px;
  cursor: pointer;
  transition: box-shadow 0.2s, transform 0.2s;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.agent-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  transform: translateY(-2px);
}

.agent-card-header { display: flex; flex-direction: column; gap: 6px; }
.agent-name-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}
.agent-name {
  font-size: 15px;
  font-weight: 700;
  color: #111;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.platform-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px;
  font-weight: 700;
  padding: 2px 7px;
  flex-shrink: 0;
  letter-spacing: 0.3px;
}
.platform-badge.reddit { background: rgba(255,69,0,0.1); color: #ff4500; }
.platform-badge.twitter { background: rgba(29,161,242,0.1); color: #1da1f2; }

.type-badge {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.3px;
  padding: 2px 7px;
  border-radius: 2px;
  text-transform: uppercase;
}
.type-badge.large { font-size: 11px; padding: 4px 10px; }

.agent-bio {
  font-size: 12px;
  line-height: 1.6;
  color: #666;
  flex: 1;
}

.agent-motivation {
  display: flex;
  flex-direction: column;
  gap: 3px;
  background: #f9f9f9;
  padding: 8px 10px;
  border-left: 2px solid #ddd;
}
.motivation-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #aaa;
}
.motivation-text {
  font-size: 11px;
  color: #555;
  line-height: 1.4;
}

.agent-card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 8px;
  border-top: 1px solid #f0f0f0;
}
.username-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: #bbb;
}
.expand-hint {
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px;
  color: #ccc;
}
.agent-card:hover .expand-hint { color: #666; }

/* ===== Modal ===== */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  backdrop-filter: blur(4px);
  padding: 20px;
}
.modal-content {
  background: #fff;
  width: 580px;
  max-width: 100%;
  max-height: 85vh;
  overflow-y: auto;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.15);
}
.modal-header {
  position: relative;
  padding: 24px 28px 20px;
  border-bottom: 1px solid #f0f0f0;
}
.modal-title-row {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 4px;
  padding-right: 40px;
}
.modal-name {
  font-size: 1.3rem;
  font-weight: 700;
  color: #111;
}
.modal-username {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: #aaa;
}
.modal-close {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 32px;
  height: 32px;
  border: none;
  background: transparent;
  font-size: 1.4rem;
  color: #aaa;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  border-radius: 4px;
}
.modal-close:hover { background: #f0f0f0; color: #111; }

.modal-body { padding: 24px 28px; display: flex; flex-direction: column; gap: 20px; }
.modal-section { display: flex; flex-direction: column; gap: 8px; }
.modal-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: #aaa;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 600;
}
.modal-text {
  font-size: 13px;
  line-height: 1.7;
  color: #333;
  background: #f9f9f9;
  padding: 14px 16px;
  border: 1px solid #f0f0f0;
  white-space: pre-wrap;
}
.modal-text.other-info { font-family: 'JetBrains Mono', monospace; font-size: 12px; }
.modal-text.mono { font-family: 'JetBrains Mono', monospace; font-size: 12px; }

/* ===== Modal transitions ===== */
.modal-enter-active, .modal-leave-active { transition: opacity 0.25s ease; }
.modal-enter-from, .modal-leave-to { opacity: 0; }
.modal-enter-active .modal-content { transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); }
.modal-leave-active .modal-content { transition: all 0.2s ease-in; }
.modal-enter-from .modal-content { transform: scale(0.95) translateY(10px); opacity: 0; }
.modal-leave-to .modal-content { transform: scale(0.95) translateY(10px); opacity: 0; }

/* ===== Responsive ===== */
@media (max-width: 768px) {
  .header-center { display: none; }
  .filter-bar { gap: 10px; }
  .search-input { width: 140px; }
  .filter-meta { display: none; }
  .agents-grid { grid-template-columns: 1fr; }
  .stats-bar { gap: 12px; }
}
</style>
