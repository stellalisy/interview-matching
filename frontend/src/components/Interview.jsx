import React from "react";
import axios from 'axios'
import { Login, Signup, TopHeader, Interviewee, Interviewer, Admin, UserInfo, Success } from './interview/index'
import '../css/styles.css'
import '../css/normalize.css'

class Interview extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user: null, // user's role: Interviewee | Interviewer | Admin
      success: false,
      info: {},
    };

    this.setUser = this.setUser.bind(this);
    this.signout = this.signout.bind(this);
    this.onSuccess = this.onSuccess.bind(this);
    this.onBack = this.onBack.bind(this);
  }

  setUser(user) {
    this.setState({ user })
  }

  login = async (user) => {
    // var { data: data } = await axios.get('/get-time')
    var data = {
      // "end_date": "2020-07-18",
      // "end_time": 38,
      // "event": "HopHacks Fall 2020 Interview",
      "days": 7,
      "hours": 7,
      "start_date": "2020-07-15",
      "start_time": 31
    }
    this.setState({ user, info: data })
  }

  async signout() {
    try {
      await axios.get('/user/signout')
      this.setState({ user: null, success: false })
    } catch (err) {
      console.log(err)
    }
  }

  onSuccess() {
    this.setState({ success: true })
  }

  onBack() {
    this.setState({ success: false })
  }

  render() {
    var { user, success } = this.state
    var role = user && user.role
    var User

    if (role === 'Interviewee') {
      User = <Interviewee {...this.state.info} callback={this.onSuccess} />
    } else if (role === 'Interviewer') {
      User = <Interviewer  {...this.state.info} callback={this.onSuccess} />
    } else if (role === 'Admin') {
      User = <Admin callback={this.onSuccess} />
    }

    return (
      <div>
        <TopHeader role={role} />

        <div className="card-wrapper">
          {
            user ?
              (success ?
                <Success callback={this.signout} back={this.onBack} /> :
                <>
                  <UserInfo  {...user} callback={this.signout} />
                  {User}
                </>
              ) :
              <>
                <Signup callback={this.setUser} />
                <Login callback={this.login} />
              </>
          }
        </div>
      </div>
    )
  };
}

export default Interview