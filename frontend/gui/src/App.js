import React, { Component} from 'react';
import 'antd/dist/antd.css'

import CustomLayout from './containers/Layout';
import PlayerList from './containers/PlayerListView'

class App extends Component {
  render() {
  return (
    <div className="App">
        <CustomLayout>
            <PlayerList />
        </CustomLayout>
    </div>
  );
}
}

export default App;
