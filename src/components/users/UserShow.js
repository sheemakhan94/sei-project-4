import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import EntryForm from '../entries/EntryForm'

class UserShow extends React.Component {
  constructor() {
    super()

    this.state = { users: null }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    this.getData()
  }

  getData() {
    console.log(this.props.match.params.id)
    axios.get('/api/profile', {
      headers: { 'Authorization': `${Auth.getToken()}` } })
      .then(res => this.setState({ user: res.data }))
      .catch(err => console.log(err))
  }

  handleChange(e) {
    this.setState({ entry: {what: e.target.value} })
  }

  handleSubmit(e) {
    e.preventDefault()
  }

  isOwner() {
    return Auth.getPayload().sub === this.state.user._id
  }

  render() {
    if (!this.state.user) return null
    const { user } = this.state
    console.log('user', user)
    const todaysTasks = user.user_tasks.filter(task => new Date(task.due).toLocaleDateString() === new Date().toLocaleDateString())
    const todaysEntry = user.user_entries.filter(entry => new Date(entry.date).toLocaleDateString() === new Date().toLocaleDateString())
    const todaysEvents = user.user_events.filter(event => new Date(event.event_date).toLocaleDateString() === new Date().toLocaleDateString())
    this.isOwner()
    return(
      <main>
        <div className="app-title-profile">
        </div>
        <div className="home-title">
          <h1>Hi {user.username}, this is your day</h1>
        </div>
        <div className="entry">
          <h3>{'Today\'s entry'}</h3>
          {!todaysEntry &&
              <EntryForm />
          }
          { todaysEntry &&
            <p>{todaysEntry[0].what}</p>
          }
        </div>
        <div className="tasks-due">
          <h3>Task(s) due today</h3>
          {todaysTasks.map(task => (
            <p key={task.id}>{task.title}</p>
          ))}
        </div>
        <div className="events-due">
          <h3>Happening today</h3>
          {todaysEvents.map(event => (
            <p key={event.id}>{event.event_name}</p>
          ))}
        </div>
      </main>
    )
  }
}
export default UserShow
