import React, { useEffect, useState } from 'react';
import TodoForm from './TodoForm';
import TodoList from './TodoList';

const TodoApp = () => {
  const URL = 'http://localhost:5340/tasks';
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      const response = await fetch(URL);
      if (!response.ok) throw new Error('Errore nella risposta del server');
      const data = await response.json();
      setTasks(data);
      setError(null);
    } catch (err) {
      setError('Errore nel caricamento');
    } finally {
      setLoading(false);
    }
  };

  const handleAddTask = async (text) => {
    if (!text.trim()) {
      setError('Il testo del task non può essere vuoto');
      return;
    }
    try {
      await fetch(URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, completed: false }),
      });
      fetchTasks();
    } catch (err) {
      setError('Errore nell’aggiunta del task');
    }
  };

  const handleDeleteTask = async (id) => {
    try {
      await fetch(`${URL}/${id}`, { method: 'DELETE' });
      fetchTasks();
    } catch (err) {
      setError('Errore nell’eliminazione del task');
    }
  };

  const handleToggleTask = async (id, completed) => {
    try {
      await fetch(`${URL}/${id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ completed: !completed }),
      });
      fetchTasks();
    } catch (err) {
      setError('Errore nell’aggiornamento del task');
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4"> To-Do List</h1>
      {error && <div className="alert alert-danger">{error}</div>}
      <TodoForm handleAddTask={handleAddTask} />
      {loading ? (
        <div className="text-center">Caricamento...</div>
      ) : (
        <TodoList
          tasks={tasks}
          handleDeleteTask={handleDeleteTask}
          handleToggleTask={handleToggleTask}
        />
      )}
    </div>
  );
};

export default TodoApp;
