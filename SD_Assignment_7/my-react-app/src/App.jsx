import axios from 'axios';
import { useEffect } from 'react';
import { useState } from 'react';
import Card from './Card';

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get("https://jsonplaceholder.typicode.com/users")
      .then(res => setUsers(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h2>User List</h2>
      {users.map(user => (
        <Card key={user.id} name={user.name} />
      ))}
    </div>
  );
}
export default App;