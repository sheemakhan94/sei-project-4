import React from 'react'
import axios from 'axios'
import mobiscroll from '@mobiscroll/react'


class EntryIndex extends React.Component {
  constructor(props) {
    super(props)

    this.state = { entries: null }

    this.onEventSelect = this.onEventSelect.bind(this)
    // this.data = this.data.bind(this)
  }

  componentDidMount() {
    axios.get('/api/entries')
      .then(res => {
        const entries = res.data.map(entry => (
          { d: new Date(entry.date), color: '#46c4f3', text: 'View entry', id: entry.id }
        ))
        console.log('entries', entries)
        this.setState({ entries })
      })
      .catch(err => console.log(err))
    console.log('state', this.state)

  }

  onEventSelect(e) {
    // console.log(e)
    this.props.history.push(`/entries/${e.event.id}`)
  }

  render() {
    if(!this.state.entries) return null
    console.log(this.state.entries)
    return(
      <main>
        <mobiscroll.Eventcalendar
          theme="ios"
          display="inline"
          calendarHeight={614}
          view={{
            calendar: {
              labels: true
            }
          }}
          onEventSelect={this.onEventSelect}
          data={this.state.entries}
        />
      </main>
    )
  }
}

export default EntryIndex
