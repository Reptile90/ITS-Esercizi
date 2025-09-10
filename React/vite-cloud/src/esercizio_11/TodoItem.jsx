import React from 'react'

const TodoItem = ({ task, handleDeleteTask, handleToggleTask }) => {
    return (
        <li
            className={`list-group-item d-flex justify-content-between align-items-center ${task.completed ? 'list-group-item-success' : ''
                }`}
        >
            <div className="form-check">
                <input
                    className="form-check-input me-2"
                    type="checkbox"
                    checked={task.completed}
                    onChange={() => handleToggleTask(task.id, task.completed)}
                />
                <label
                    className={`form-check-label ${task.completed ? 'text-decoration-line-through' : ''
                        }`}
                >
                    {task.text}
                </label>
            </div>
            <button
                className="btn btn-sm btn-danger"
                onClick={() => handleDeleteTask(task.id)}
            >
                Elimina
            </button>
        </li>
    )
}

export default TodoItem