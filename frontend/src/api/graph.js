import service, { requestWithRetry } from './index'

/**
 * Generate ontology (upload documents and simulation requirement)
 * @param {Object} data - Contains files, simulation_requirement, project_name, etc.
 * @returns {Promise}
 */
export function generateOntology(formData) {
  return requestWithRetry(() => 
    service({
      url: '/api/graph/ontology/generate',
      method: 'post',
      data: formData,
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
  )
}

/**
 * Build graph
 * @param {Object} data - Contains project_id, graph_name, etc.
 * @returns {Promise}
 */
export function buildGraph(data) {
  return requestWithRetry(() =>
    service({
      url: '/api/graph/build',
      method: 'post',
      data
    })
  )
}

/**
 * Query task status
 * @param {String} taskId - Task ID
 * @returns {Promise}
 */
export function getTaskStatus(taskId) {
  return service({
    url: `/api/graph/task/${taskId}`,
    method: 'get'
  })
}

/**
 * Get graph data
 * @param {String} graphId - Graph ID
 * @returns {Promise}
 */
export function getGraphData(graphId) {
  return service({
    url: `/api/graph/data/${graphId}`,
    method: 'get'
  })
}

/**
 * Get project info
 * @param {String} projectId - Project ID
 * @returns {Promise}
 */
export function getProject(projectId) {
  return service({
    url: `/api/graph/project/${projectId}`,
    method: 'get'
  })
}

/**
 * Get seed files for a project
 * @param {String} projectId - Project ID
 * @returns {Promise}
 */
export function getProjectFiles(projectId) {
  return service({
    url: `/api/graph/project/${projectId}/files`,
    method: 'get'
  })
}

/**
 * Update a seed file's content
 * @param {String} projectId - Project ID
 * @param {String} filename - Filename to update
 * @param {String} content - New content
 * @returns {Promise}
 */
export function updateProjectFile(projectId, filename, content) {
  return service({
    url: `/api/graph/project/${projectId}/files/${encodeURIComponent(filename)}`,
    method: 'put',
    data: { content },
    headers: { 'Content-Type': 'application/json' }
  })
}
