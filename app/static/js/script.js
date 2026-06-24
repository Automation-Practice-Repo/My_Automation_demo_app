// API Helper Functions
const API = {
    getTasks: async (params = {}) => {
        const query = new URLSearchParams(params).toString();
        const response = await fetch(`/api/tasks?${query}`);
        return response.json();
    },

    createTask: async (taskData) => {
        const response = await fetch('/api/tasks', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(taskData)
        });
        return response.json();
    },

    updateTask: async (taskId, taskData) => {
        const response = await fetch(`/api/tasks/${taskId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(taskData)
        });
        return response.json();
    },

    deleteTask: async (taskId) => {
        const response = await fetch(`/api/tasks/${taskId}`, {
            method: 'DELETE'
        });
        return response.json();
    },

    getStats: async () => {
        const response = await fetch('/api/stats');
        return response.json();
    }
};

// Utility Functions
const Utils = {
    formatDate: (dateString) => {
        const date = new Date(dateString);
        return date.toLocaleDateString();
    },

    showNotification: (message, type = 'info') => {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type}`;
        alertDiv.innerHTML = `
            ${message}
            <button onclick="this.parentElement.style.display='none';">&times;</button>
        `;
        document.querySelector('.container').insertBefore(alertDiv, document.querySelector('.container').firstChild);

        setTimeout(() => {
            alertDiv.style.display = 'none';
        }, 5000);
    }
};

// DOM ready
document.addEventListener('DOMContentLoaded', function() {
    // Add any additional initialization code here
    console.log('My Auto Prac app loaded');
});
