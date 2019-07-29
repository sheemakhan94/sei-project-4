import React from 'react'
import axios from 'axios'
import mobiscroll from '@mobiscroll/react'


class EventsIndex extends React.Component {
  constructor(props) {
    super(props)

    this.state = { events: null }

    this.onEventSelect = this.onEventSelect.bind(this)
    // this.data = this.data.bind(this)
  }

  componentDidMount() {
    axios.get('/api/events')
      .then(res => {
        const events = res.data.map(event => (
          { d: new Date(event.date), color: '#46c4f3', text: event.event_name, id: event.id }
        ))
        console.log('events', events)
        this.setState({ events })
      })
      .catch(err => console.log(err))
    console.log('state', this.state)

  }

  onEventSelect(e) {
    // console.log(e)
    this.props.history.push(`/events/${e.event.id}`)
  }

  render() {
    if(!this.state.events) return null
    console.log(this.state.events)
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
          data={this.state.events}
        />
      </main>
    )
  }
}

export default EventsIndex
