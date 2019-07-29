import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

class Login extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, errors: {} }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange({ target: {name, value} }) {
    const data = { ...this.state.data, [name]: value }
    const errors = { ...this.state.errors, [name]: ''}
    this.setState({ data, errors })
    console.log(data, errors)
  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('api/login', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)
        this.props.history.push('/profile')
      })
      .catch(() => this.setState({ error: 'Invalid Crendentials' }))
  }

  render() {
    return(
      <main>
        <section className="form-container">
          <form onSubmit={this.handleSubmit}>
            <h2 className="form-title">Log In</h2>
            <div className="field">
              <div className="control">
                <input
                  className="input"
                  name="email"
                  placeholder="Email"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="field">
              <div className="control">
                <input
                  className="input"
                  type="password"
                  name="password"
                  placeholder="Password"
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <button type="submit" className="button">Log In</button>
          </form>
        </section>
      </main>
    )
  }
}

export default Login
