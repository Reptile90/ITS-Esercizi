import React from 'react'
import { Link, Outlet } from 'react-router-dom'

const Profile = () => {
  return (
    <div>
        <h1>PROFILE</h1>
        <nav>
            <Link to="me">Il mio profilo</Link>
            <Link to="/profile/2">Il mio profilo 2</Link>
        </nav>
        <div>
            <Outlet></Outlet>
        </div>
    </div>
  )
}

export default Profile