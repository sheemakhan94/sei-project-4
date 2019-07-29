import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import Moment from 'react-moment'
import Auth from '../../lib/Auth'

class EntryShow extends React.Component {
  constructor() {
    super()

    this.state = { entry: null }

    this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {
    this.getData()
  }

  getData() {
    axios.get(`/api/entries/${this.props.match.params.id}`)
      .then(res => this.setState({ entry: res.data }))
      .catch(err => console.log(err))
  }

  handleDelete() {
    axios.delete(`/api/entries/${this.props.match.params.id}`, {
      headers: { Authorization: `Bearer ${Auth.getToken()}` }
    })
      .then(() => this.props.history.push('/entries'))
      .catch(err => console.log(err.response))
  }

  render() {
    if(!this.state.entry) return null
    const { entry } = this.state
    return(
      <main>
        <div className="entry-date">
          <Moment format="DD/MM/YY">{entry.date}</Moment>
        </div>
        <div className="entry-text">
          <p>{entry.what}</p>
        </div>
        <section className="buttons">
          <div className="edit-button">
            <Link className="button" to={`/entries/${entry.id}/edit`}>Edit</Link>
          </div>
          <div className="delete-button">
            <button className="button" onClick={this.handleDelete}>Delete entry</button>
          </div>
        </section>
      </main>
    )
  }
}

export default EntryShow
