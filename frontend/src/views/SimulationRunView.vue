<template>
  <div class="main-view">
    <!-- Header -->
    <header class="app-header">
      <div class="header-left">
        <div class="brand" @click="router.push('/')">MIROFISH</div>
      </div>
      
      <div class="header-center">
        <div class="view-switcher">
          <button 
            v-for="mode in ['graph', 'split', 'workbench']" 
            :key="mode"
            class="switch-btn"
            :class="{ active: viewMode === mode }"
            @click="viewMode = mode"
          >
            {{ { graph: 'Graph', split: 'Split', workbench: 'Workbench' }[mode] }}
          </button>
        </div>
      </div>

      <div class="header-right">
        <button class="brief-btn" @click="briefOpen = !briefOpen" :class="{ active: briefOpen }">
          <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          Brief
        </button>
        <div class="step-divider"></div>
        <div v-if="llmModel" class="model-badge">
          <svg viewBox="0 0 24 24" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"></path></svg>
          {{ llmModel }}
        </div>
        <div class="step-divider"></div>
        <div class="workflow-step">
          <span class="step-num">Step 3/5</span>
          <span class="step-name">Start Simulation</span>
        </div>
        <div class="step-divider"></div>
        <span class="status-indicator" :class="statusClass">
          <span class="dot"></span>
          {{ statusText }}
        </span>
      </div>
    </header>

    <!-- Brief Drawer -->
    <transition name="drawer">
      <div v-if="briefOpen" class="brief-drawer">
        <div class="brief-drawer-header">
          <span class="brief-drawer-title">Simulation Brief</span>
          <button class="brief-close" @click="briefOpen = false">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          </button>
        </div>
        <div class="brief-drawer-body">
          <div class="brief-meta-row">
            <div class="brief-meta-item">
              <span class="brief-meta-label">Model</span>
              <span class="brief-meta-value mono">{{ llmModel || '—' }}</span>
            </div>
            <div class="brief-meta-item">
              <span class="brief-meta-label">Agents</span>
              <span class="brief-meta-value mono">{{ simAgentCount || '—' }}</span>
            </div>
            <div class="brief-meta-item">
              <span class="brief-meta-label">Duration</span>
              <span class="brief-meta-value mono">{{ simHours ? simHours + 'h' : '—' }}</span>
            </div>
            <div class="brief-meta-item">
              <span class="brief-meta-label">Round</span>
              <span class="brief-meta-value mono">{{ minutesPerRound }}min</span>
            </div>
          </div>
          <div class="brief-requirement-label">Simulation Requirement</div>
          <div class="brief-requirement-text">{{ simulationRequirement || 'No requirement defined.' }}</div>
        </div>
      </div>
    </transition>

    <!-- Main Content Area -->
    <main class="content-area">
      <!-- Left Panel: Graph -->
      <div class="panel-wrapper left" :style="leftPanelStyle">
        <GraphPanel 
          :graphData="graphData"
          :loading="graphLoading"
          :currentPhase="3"
          :isSimulating="isSimulating"
          @refresh="refreshGraph"
          @toggle-maximize="toggleMaximize('graph')"
        />
      </div>

      <!-- Right Panel: Step3 Start Simulation -->
      <div class="panel-wrapper right" :style="rightPanelStyle">
        <Step3Simulation
          :simulationId="currentSimulationId"
          :maxRounds="maxRounds"
          :minutesPerRound="minutesPerRound"
          :projectData="projectData"
          :graphData="graphData"
          :systemLogs="systemLogs"
          @go-back="handleGoBack"
          @next-step="handleNextStep"
          @add-log="addLog"
          @update-status="updateStatus"
        />
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import GraphPanel from '../components/GraphPanel.vue'
import Step3Simulation from '../components/Step3Simulation.vue'
import { getProject, getGraphData } from '../api/graph'
import { getSimulation, getSimulationConfig, stopSimulation, closeSimulationEnv, getEnvStatus } from '../api/simulation'

const route = useRoute()
const router = useRouter()

// Props
const props = defineProps({
  simulationId: String
})

// Layout State
const viewMode = ref('split')
const briefOpen = ref(false)

// Data State
const currentSimulationId = ref(route.params.simulationId)
// Get maxRounds from query params at init time so child components can access it immediately
const maxRounds = ref(route.query.maxRounds ? parseInt(route.query.maxRounds) : null)
const minutesPerRound = ref(30) // Default: 30 min per round
const projectData = ref(null)
const graphData = ref(null)
const graphLoading = ref(false)
const systemLogs = ref([])
const currentStatus = ref('processing') // processing | completed | error

// Brief / model info
const llmModel = ref(null)
const simulationRequirement = ref(null)
const simAgentCount = ref(null)
const simHours = ref(null)


// --- Computed Layout Styles ---
const leftPanelStyle = computed(() => {
  if (viewMode.value === 'graph') return { width: '100%', opacity: 1, transform: 'translateX(0)' }
  if (viewMode.value === 'workbench') return { width: '0%', opacity: 0, transform: 'translateX(-20px)' }
  return { width: '50%', opacity: 1, transform: 'translateX(0)' }
})

const rightPanelStyle = computed(() => {
  if (viewMode.value === 'workbench') return { width: '100%', opacity: 1, transform: 'translateX(0)' }
  if (viewMode.value === 'graph') return { width: '0%', opacity: 0, transform: 'translateX(20px)' }
  return { width: '50%', opacity: 1, transform: 'translateX(0)' }
})

// --- Status Computed ---
const statusClass = computed(() => {
  return currentStatus.value
})

const statusText = computed(() => {
  if (currentStatus.value === 'error') return 'Error'
  if (currentStatus.value === 'completed') return 'Completed'
  return 'Running'
})

const isSimulating = computed(() => currentStatus.value === 'processing')

// --- Helpers ---
const addLog = (msg) => {
  const time = new Date().toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' }) + '.' + new Date().getMilliseconds().toString().padStart(3, '0')
  systemLogs.value.push({ time, msg })
  if (systemLogs.value.length > 200) {
    systemLogs.value.shift()
  }
}

const updateStatus = (status) => {
  currentStatus.value = status
}

// --- Layout Methods ---
const toggleMaximize = (target) => {
  if (viewMode.value === target) {
    viewMode.value = 'split'
  } else {
    viewMode.value = target
  }
}

const handleGoBack = async () => {
  // Before going back to Step 2, close any running simulation
  addLog('Preparing to go back to Step 2, closing simulation...')
  
  // Stop polling
  stopGraphRefresh()
  
  try {
    // Try graceful shutdown first
    const envStatusRes = await getEnvStatus({ simulation_id: currentSimulationId.value })
    
    if (envStatusRes.success && envStatusRes.data?.env_alive) {
      addLog('Closing simulation environment...')
      try {
        await closeSimulationEnv({ 
          simulation_id: currentSimulationId.value,
          timeout: 10
        })
        addLog('✓ Simulation environment closed')
      } catch (closeErr) {
        addLog(`Failed to close environment, forcing stop...`)
        try {
          await stopSimulation({ simulation_id: currentSimulationId.value })
          addLog('✓ Simulation force stopped')
        } catch (stopErr) {
          addLog(`Force stop failed: ${stopErr.message}`)
        }
      }
    } else {
      // Environment not running, check if process needs to be stopped
      if (isSimulating.value) {
        addLog('Stopping simulation process...')
        try {
          await stopSimulation({ simulation_id: currentSimulationId.value })
          addLog('✓ Simulation stopped')
        } catch (err) {
          addLog(`Stop simulation failed: ${err.message}`)
        }
      }
    }
  } catch (err) {
    addLog(`Failed to check simulation status: ${err.message}`)
  }
  
  // Go back to Step 2 (Environment Setup)
  router.push({ name: 'Simulation', params: { simulationId: currentSimulationId.value } })
}

const handleNextStep = () => {
  // Step3Simulation component handles report generation and routing directly
  // This method is a fallback
  addLog('Entering Step 4: Report Generation')
}

// --- Data Logic ---
const loadSimulationData = async () => {
  try {
    addLog(`Loading simulation data: ${currentSimulationId.value}`)
    
    const simRes = await getSimulation(currentSimulationId.value)
    if (simRes.success && simRes.data) {
      const simData = simRes.data
      
      // Get simulation config for minutes_per_round + brief info
      try {
        const configRes = await getSimulationConfig(currentSimulationId.value)
        if (configRes.success && configRes.data) {
          const cfg = configRes.data
          if (cfg.time_config?.minutes_per_round) {
            minutesPerRound.value = cfg.time_config.minutes_per_round
            addLog(`Time config: ${minutesPerRound.value} min/round`)
          }
          if (cfg.time_config?.total_simulation_hours) {
            simHours.value = cfg.time_config.total_simulation_hours
          }
          if (cfg.agent_configs?.length) {
            simAgentCount.value = cfg.agent_configs.length
          }
          if (cfg.llm_model) {
            llmModel.value = cfg.llm_model
          }
          if (cfg.simulation_requirement) {
            simulationRequirement.value = cfg.simulation_requirement
          }
        }
      } catch (configErr) {
        addLog(`Failed to get time config, using default: ${minutesPerRound.value} min/round`)
      }
      
      // Also check project for simulation_requirement if config didn't have it
      if (!simulationRequirement.value && projectData.value?.simulation_requirement) {
        simulationRequirement.value = projectData.value.simulation_requirement
      }
      
      if (simData.project_id) {
        const projRes = await getProject(simData.project_id)
        if (projRes.success && projRes.data) {
          projectData.value = projRes.data
          addLog(`Project loaded: ${projRes.data.project_id}`)
          
          // Fallback: get simulation_requirement from project if config didn't have it
          if (!simulationRequirement.value && projRes.data.simulation_requirement) {
            simulationRequirement.value = projRes.data.simulation_requirement
          }

          if (projRes.data.graph_id) {
            await loadGraph(projRes.data.graph_id)
          }
        }
      }
    } else {
      addLog(`Failed to load simulation data: ${simRes.error || 'Unknown error'}`)
    }
  } catch (err) {
    addLog(`Load error: ${err.message}`)
  }
}

const loadGraph = async (graphId) => {
  // Skip full-screen loading during active simulation to avoid flickering
  // Show loading on manual refresh or initial load
  if (!isSimulating.value) {
    graphLoading.value = true
  }
  
  try {
    const res = await getGraphData(graphId)
    if (res.success) {
      graphData.value = res.data
      if (!isSimulating.value) {
        addLog('Graph data loaded')
      }
    }
  } catch (err) {
    addLog(`Graph load failed: ${err.message}`)
  } finally {
    graphLoading.value = false
  }
}

const refreshGraph = () => {
  if (projectData.value?.graph_id) {
    loadGraph(projectData.value.graph_id)
  }
}

// --- Auto Refresh Logic ---
let graphRefreshTimer = null

const startGraphRefresh = () => {
  if (graphRefreshTimer) return
  addLog('Live graph refresh enabled (30s)')
  graphRefreshTimer = setInterval(refreshGraph, 30000)
}

const stopGraphRefresh = () => {
  if (graphRefreshTimer) {
    clearInterval(graphRefreshTimer)
    graphRefreshTimer = null
    addLog('Live graph refresh stopped')
  }
}

watch(isSimulating, (newValue) => {
  if (newValue) {
    startGraphRefresh()
  } else {
    stopGraphRefresh()
  }
}, { immediate: true })

onMounted(() => {
  addLog('SimulationRunView initialized')
  
  if (maxRounds.value) {
    addLog(`Custom round limit: ${maxRounds.value}`)
  }
  
  loadSimulationData()
})

onUnmounted(() => {
  stopGraphRefresh()
})
</script>

<style scoped>
.main-view {
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: #FFF;
  overflow: hidden;
  font-family: 'Space Grotesk', 'Noto Sans SC', system-ui, sans-serif;
}

/* Header */
.app-header {
  height: 60px;
  border-bottom: 1px solid #EAEAEA;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  background: #FFF;
  z-index: 100;
  position: relative;
}

.header-center {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}

.brand {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 800;
  font-size: 18px;
  letter-spacing: 1px;
  cursor: pointer;
}

.view-switcher {
  display: flex;
  background: #F5F5F5;
  padding: 4px;
  border-radius: 6px;
  gap: 4px;
}

.switch-btn {
  border: none;
  background: transparent;
  padding: 6px 16px;
  font-size: 12px;
  font-weight: 600;
  color: #666;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
}

.switch-btn.active {
  background: #FFF;
  color: #000;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.header-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.workflow-step {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
}

.step-num {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  color: #999;
}

.step-name {
  font-weight: 700;
  color: #000;
}

.step-divider {
  width: 1px;
  height: 14px;
  background-color: #E0E0E0;
}

.status-indicator {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: #666;
  font-weight: 500;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #CCC;
}

.status-indicator.processing .dot { background: #FF5722; animation: pulse 1s infinite; }
.status-indicator.completed .dot { background: #4CAF50; }
.status-indicator.error .dot { background: #F44336; }

@keyframes pulse { 50% { opacity: 0.5; } }

/* Content */
.content-area {
  flex: 1;
  display: flex;
  position: relative;
  overflow: hidden;
}

.panel-wrapper {
  height: 100%;
  overflow: hidden;
  transition: width 0.4s cubic-bezier(0.25, 0.8, 0.25, 1), opacity 0.3s ease, transform 0.3s ease;
  will-change: width, opacity, transform;
}

.panel-wrapper.left {
  border-right: 1px solid #EAEAEA;
}

/* Brief button */
.brief-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border: 1px solid #E0E0E0;
  background: #FFF;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  color: #444;
  cursor: pointer;
  transition: all 0.15s;
}
.brief-btn:hover { background: #F5F5F5; border-color: #CCC; }
.brief-btn.active { background: #000; color: #FFF; border-color: #000; }
.brief-btn.active svg { stroke: #FFF; }

/* Model badge */
.model-badge {
  display: flex;
  align-items: center;
  gap: 5px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 600;
  color: #666;
  background: #F5F5F5;
  border: 1px solid #E8E8E8;
  padding: 4px 10px;
  border-radius: 20px;
  white-space: nowrap;
}

/* Brief Drawer */
.brief-drawer {
  position: absolute;
  top: 60px;
  right: 0;
  width: 420px;
  max-width: 100vw;
  background: #FFF;
  border-left: 1px solid #EAEAEA;
  border-bottom: 1px solid #EAEAEA;
  z-index: 200;
  box-shadow: -4px 4px 20px rgba(0,0,0,0.08);
  display: flex;
  flex-direction: column;
  max-height: calc(100vh - 60px);
}

.brief-drawer-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 20px;
  border-bottom: 1px solid #F0F0F0;
  flex-shrink: 0;
}

.brief-drawer-title {
  font-size: 13px;
  font-weight: 700;
  color: #000;
  letter-spacing: 0.3px;
}

.brief-close {
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  color: #999;
  display: flex;
  align-items: center;
  border-radius: 4px;
  transition: background 0.15s;
}
.brief-close:hover { background: #F5F5F5; color: #333; }

.brief-drawer-body {
  overflow-y: auto;
  padding: 20px;
  flex: 1;
}

.brief-meta-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 20px;
}

.brief-meta-item {
  background: #F9F9F9;
  border: 1px solid #EFEFEF;
  border-radius: 8px;
  padding: 10px 14px;
}

.brief-meta-label {
  display: block;
  font-size: 10px;
  font-weight: 700;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}

.brief-meta-value {
  font-size: 14px;
  font-weight: 600;
  color: #111;
}
.brief-meta-value.mono {
  font-family: 'JetBrains Mono', monospace;
}

.brief-requirement-label {
  font-size: 11px;
  font-weight: 700;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 10px;
}

.brief-requirement-text {
  font-size: 13px;
  line-height: 1.7;
  color: #333;
  white-space: pre-wrap;
  word-break: break-word;
}

/* Drawer transition */
.drawer-enter-active, .drawer-leave-active {
  transition: transform 0.25s cubic-bezier(0.25, 0.8, 0.25, 1), opacity 0.2s ease;
}
.drawer-enter-from, .drawer-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>

