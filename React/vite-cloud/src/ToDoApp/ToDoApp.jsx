import React, { useState ,useEffect} from 'react'
import ToDoForm from './ToDoForm'
import ToDoList from './ToDoList'

const API_URL = '/api/tasks'
const ToDoApp = () => {
    const [tasks,setTasks]= useState([]);
    const [loading,setLoading]= useState(true);
    const [error, setError]= useState(null);


    const fetchTasks = async ()=>{
        try{
            const response = await fetch(API_URL);
            if(!response.ok) throw new Error("Errore nella fetch")

            const data = await response.json();

            setTasks(data);
            

        }
        catch(err){
            setError(err)

        }
        finally{
            setLoading(false)

        }
    }
    const deleteTask = async (id) => {
        await fetch(API_URL+ "/"+id,{method:"DELETE"})
        fetchTasks();

    }


    const toogleTask = async(id,completed)=>{
        await fetch(API_URL + "/" + id, {
            method:"PATCH",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({completed:!completed})})
        fetchTasks();
    }
    useEffect(()=>{
        fetchTasks();
    },[]);
    return (
        <div>
            <ToDoForm></ToDoForm> 
            <ToDoList tasks={tasks} onDeleteTask ={deleteTask} onToggleTask ={toogleTask}></ToDoList>
        </div>
    )
}

export default ToDoApp