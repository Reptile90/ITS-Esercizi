import React from 'react';
import TodoItem from './TodoItem';

const TodoList = ({ tasks, handleDeleteTask, handleToggleTask }) => {
  return (
    <div>
      <ul className="list-group">
        {tasks.map((task) => (
          <TodoItem
            key={task.id}
            task={task}
            handleDeleteTask={handleDeleteTask}
            handleToggleTask={handleToggleTask}
          />
        ))}
      </ul>
    </div>
  );
};

export default TodoList;
