import React, { useState } from 'react';

const TodoForm = ({ handleAddTask }) => {
    const [text, setText] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (text.trim()) {
            handleAddTask(text);
            setText('');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="mb-4">
            <div className="input-group">
                <input
                    type="text"
                    className="form-control"
                    placeholder="Nuovo task"
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                />
                <button className="btn btn-primary" type="submit">
                    Aggiungi
                </button>
            </div>
        </form>
    );
};

export default TodoForm;
