import React from 'react'

class EventForm extends React.Component {
  render() {
    return(
      <main className="form-container">
        <form>
          <div className="control">
            <input
              className="input"
              name="event-name"
              placeholder="Event Name"
            />
          </div>
          <div className="control">
            <input
              type="date"
              className="input"
              name="event-date"
            />
          </div>
          <div className="control">
            <input
              className="input"
              name="event-location"
              placeholder="Event Location"
            />
          </div>
        </form>
      </main>
    )
  }
}

export default EventForm
