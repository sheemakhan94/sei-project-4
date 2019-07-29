import React from 'react'

const TaskForm = ({ newTask, due, handleChange, handleSubmit }) => {
  return (
    <form onSubmit={handleSubmit}>
      <input
        onChange={handleChange}
        name="task"
        placeholder="Title"
        value={newTask}
      />
      <input
        type="date"
        onChange={handleChange}
        name="due-date"
        placeholder="due by"
        value={due}
      />
      <button>Submit</button>
    </form>
  )
}

export default TaskForm
