import React from 'react'
import axios from 'axios'

import TaskCard from './TaskCard'
import TaskForm from './TaskForm'

class TasksIndex extends React.Component {
  constructor() {
    super()

    this.state = { tasks: null, newTask: '' }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    axios.get('/api/tasks')
      .then(res => this.setState({ tasks: res.data }))
      .catch(err => console.log(err))
  }

  handleChange(e) {
    this.setState({ newTask: e.target.value })
  }

  handleSubmit(e) {
    e.preventDefault()

    if(!this.state.newTask) return
    const task = { task: this.state.to_do, completed: false }
    const tasksRemaining = { ...this.state.tasks, task}
    this.setState = { tasksRemaining, newTask: '' }
  }

  // toggleCompleted(task) {
  //   const index = this.state.tasks.indexOf(task)
  //   const tasks = this.state.tasks.map((task, i) => {
  //     if (i === index) return {...task, completed: !task.completed }
  //     return {...task}
  //   })
  //   this.setState({ tasks })
  // }

  // remainingTasks() {
  //   return this.state.tasks.filter(task => !task.completed).length
  // }

  render() {
    if(!this.state.tasks) return null
    console.log('state.tasks', this.state.tasks)
    return(
      <main>
        <div className="title">
          <h1>You have  left</h1>
        </div>
        <div className="tasks">
          {this.state.tasks.map(task =>
            <TaskCard
              key={task.id}
              {...task}/>)}
        </div>
        <TaskForm
          newTask={this.state.newTask}
          handleChange={this.handleChange}
          handleSubmit={this.handleSubmit}
        />
      </main>
    )
  }
}


export default TasksIndex
