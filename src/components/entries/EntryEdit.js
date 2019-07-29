import React from 'react'
import axios from 'axios'
import EntryForm from './EntryForm'
import Auth from '../../lib/Auth'


class EntryEdit extends React.Component {
  constructor() {
    super()

    this.state = { data: { } }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    axios.get(`/api/entries/${this.props.match.params.id}`)
      .then(res => this.setState({ data: res.data }))
      .catch(err => console.log(err.response))
  }

  handleChange({ target: { name, value } }) {
    const data = { ...this.state.data, [name]: value }
    this.setState({ data })
  }

  handleSubmit(e){
    e.preventDefault()

    axios.put(`/api/entries/${this.props.match.params.id}`, this.state.data,{
      headers: { Authorization: `Bearer ${Auth.getToken()}` }
    })

      .then(() => this.props.history.push(`/entries/${this.props.match.params.id}`))
      .catch(err => console.log(err.response))
  }
  render() {
    return(
      <main>
        < EntryForm
          data={this.state.data}
          handleChange={this.handleChange}
          handleSubmit={this.handleSubmit}/>
      </main>
    )
  }
}

export default EntryEdit
