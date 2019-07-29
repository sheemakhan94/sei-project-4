import React from 'react'
import mobiscroll from '@mobiscroll/react'
import axios from 'axios'

class Calendar extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      myEvents: []
    }

    axios.get('/api/entries', (events) => {
      this.setState({ myEvents: events})
    }, 'jsonp')
  }
  render() {
    return (
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
        data={this.state.myEvents}
      />
    )
  }
}

export default Calendar
