import React from 'react'
import Moment from 'react-moment'

const TaskCard = ({ title, due, components }) => {
  console.log('comp', components)
  return(
    <main>
      <div className="task-title">
        <h3>{title}</h3>
      </div>
      <ol>
        {components.map(component => (
          <li
            key={component.id}
          >{component.step}</li>
        ))}
      </ol>
      <div>
        <Moment format="DD/MM/YY HH:mm">{due}</Moment>
      </div>
    </main>
  )
}

export default TaskCard
