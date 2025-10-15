import React, { useState, useEffect } from 'react'
import ToDoForm from './ToDoForm'
import ToDoList from './ToDoList'
import { deleteTaskService, fetchTasksService, toogleTaskService,addTaskService,updateTaskService } from './api'

const API_URL = '/api/tasks'
const ToDoApp = () => {
    const [tasks, setTasks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);


    const fetchTasks = async () => {
        try {
            const data = await fetchTasksService();
            setTasks(data)


        }
        catch (err) {
            setError(err)

        }
        finally {
            setLoading(false)

        }
    }
    const deleteTask = async (id) => {
        await deleteTaskService(id);
        fetchTasks();

    }


    const toogleTask = async (id, completed) => {
        await toogleTaskService(id,completed)
        fetchTasks();
    }

    const addTask = async (text) => {
        await addTaskService(text)
        fetchTasks();

    }

    const updateTask = async (id, text) => {
        await updateTaskService(id,text)
        fetchTasks();
    }

    useEffect(() => {
        fetchTasks();
    }, []);
    return (
        <div>
            <ToDoForm onAddTask={addTask}></ToDoForm>
            <ToDoList
                tasks={tasks}
                onDeleteTask={deleteTask}
                onToggleTask={toogleTask}
                onUpdateTask ={updateTask}>
            </ToDoList>
        </div>
    )
}

export default ToDoApp