/** @format */

import React, { Component } from "react";

class App extends Component {
  state = {
    notes: [],
  };

  async componentDidMount() {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/notes"); // fetching the data from api, before the page loaded
      const notes = await res.json();
      this.setState({ notes });
    } catch (error) {
      console.log(error);
    }
  }

  render() {
    return (
      <div>
        {this.state.notes.map((item) => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.body}</span>
            <span>{item.status}</span>
            <span>{item.completed}</span>
            <span>{item.publish}</span>
            <span>{item.created}</span>
            <span>{item.updated}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
