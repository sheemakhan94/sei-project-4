import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import Moment from 'react-moment'
import Auth from '../../lib/Auth'


class EntryShow extends React.Component {
  constructor() {
    super()

    this.state = { event: null }

    this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {
    this.getData()
  }

  getData() {
    axios.get(`/api/events/${this.props.match.params.id}`)
      .then(res => this.setState({ event: res.data }))
      .catch(err => console.log(err))
  }

  handleDelete() {
    axios.delete(`/api/events/${this.props.match.params.id}`, {
      headers: { Authorization: `Bearer ${Auth.getToken()}` }
    })
      .then(() => this.props.history.push('/events'))
      .catch(err => console.log(err.response))
  }

  render() {
    if(!this.state.event) return null
    const { event } = this.state
    return(
      <main>
        <div className="event-name">
          <h3>{event.event_name}</h3>
        </div>
        <div className="event-date">
          <Moment format="DD/MM/YY HH:mm">{event.event_date}</Moment>
        </div>
        <div className="event-location">
          <h3>{event.event_location}</h3>
        </div>
        <section className="buttons">
          <div className="edit-button">
            <Link className="button" to={`/events/${event.id}/edit`}>Edit</Link>
          </div>
          <div className="delete-button">
            <button className="button" onClick={this.handleDelete}>Delete event</button>
          </div>
        </section>
      </main>
    )
  }
}

export default EntryShow
