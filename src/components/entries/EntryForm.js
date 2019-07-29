import React from 'react'

const EntryForm = ({ handleSubmit, handleChange }) => {
  return(
    <form onSubmit={handleSubmit}>
      <textarea
        type="text"
        className="entry-text"
        name="entry-text"
        placeholder="What happened today?"
        onChange={handleChange}
      />
      <button type="submit" className="button">Add entry</button>
    </form>
  )
}


export default EntryForm
