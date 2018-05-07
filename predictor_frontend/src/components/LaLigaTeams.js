import React, { Component } from 'react';



class LaLigaTeams extends Component {
  state = {
   laligateams: [],
 };

 async componentDidMount() {
   try {
     const res = await fetch('http://127.0.0.1:8000/laliga/');
     const laligateams = await res.json();
     this.setState({
       laligateams,
     });
   } catch (e) {
     console.log(e);
   }
 }

  render() {
    return (
      <div>
          <h2> La Liga Teams </h2>
          {this.state.laligateams.map(item => (
            <div>
              <h3>{item.name}</h3>
              <p>{item.location}</p>
              <p>{item.league}</p>
            </div>
          ))}
      </div>
    );
  }
}

export default LaLigaTeams;
