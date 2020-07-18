import React from "react";

class TopHeader extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <>
        <h2 className="center"> Fall 2020 </h2>
        <h3 className="center">HopHacks Club Interview</h3>
        {this.props.role === 'Admin' ? <h1 className="center">Admin Page</h1> : ''}
      </>
    )
  }
}

export default TopHeader