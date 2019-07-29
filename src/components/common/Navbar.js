import React from 'react'
import { Link } from 'react-router-dom'

class Navbar extends React.Component {
  render () {
    return(
      <main>
        <Link to="/">Home</Link>
        <Link to="/register">Register</Link>
        <Link to="/login">Log In</Link>
        <Link to="/profile">Profile</Link>
      </main>
    )
  }
}

export default Navbar
