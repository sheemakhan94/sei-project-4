import React from 'react'
import axios from 'axios'
import EventForm from './EventForm'
import Auth from '../../lib/Auth'


class EventEdit extends React.Component {
  constructor() {
    super()

    this.state = { data: { } }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    axios.get(`/api/events/${this.props.match.params.id}`)
      .then(res => this.setState({ data: res.data }))
      .catch(err => console.log(err.response))
  }

  handleChange({ target: { name, value } }) {
    const data = { ...this.state.data, [name]: value }
    this.setState({ data })
  }

  handleSubmit(e){
    e.preventDefault()

    axios.put(`/api/events/${this.props.match.params.id}`, this.state.data,{
      headers: { Authorization: `Bearer ${Auth.getToken()}` }
    })

      .then(() => this.props.history.push(`/events/${this.props.match.params.id}`))
      .catch(err => console.log(err.response))
  }
  render() {
    return(
      <main>
        < EventForm
          data={this.state.data}
          handleChange={this.handleChange}
          handleSubmit={this.handleSubmit}/>
      </main>
    )
  }
}

export default EventEdit
