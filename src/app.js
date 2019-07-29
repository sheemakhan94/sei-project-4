import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import './style.scss'
import '@mobiscroll/react/dist/css/mobiscroll.min.css'

import Home from './components/common/Home'
import Navbar from './components/common/Navbar'
import Register from './components/auth/Register'
import Login from './components/auth/Login'
import UserShow from './components/users/UserShow'
import TasksIndex from './components/tasks/TasksIndex'
import EventsIndex from './components/events/EventsIndex'
import EventShow from './components/events/EventShow'
import EventEdit from './components/events/EventEdit'
import EntryIndex from './components/entries/EntryIndex'
import EntryShow from './components/entries/EntryShow'
import EntryEdit from './components/entries/EntryEdit'

const App = () => {
  return(
    <BrowserRouter>
      <main>
        <Navbar />
        <Switch>
          <Route path="/register" component={Register} />
          <Route path="/login" component={Login} />
          <Route path="/profile" component={UserShow} />
          <Route path="/tasks" component={TasksIndex} />
          <Route path="/events/:id/edit" component={EventEdit} />
          <Route path="/events/:id" component={EventShow} />
          <Route path="/events" component={EventsIndex} />
          <Route path="/entries/:id/edit" component={EntryEdit} />
          <Route path="/entries/:id" component={EntryShow} />
          <Route path="/entries" component={EntryIndex} />
          <Route path="/" component={Home} />
        </Switch>
      </main>
    </BrowserRouter>
  )
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
