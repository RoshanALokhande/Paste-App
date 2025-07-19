import './App.css'
import {createBrowserRouter,RouterProvider} from 'react-router-dom'
import Navbar from './components/Navbar'
import ViewPaste from './components/ViewPaste'
import Home from './components/Home'
import Pastes from './components/Pastes'

const router = createBrowserRouter(
  [
    {
      path : '/',
      element:
      <div>
        <Navbar></Navbar>
        <Home></Home>
      </div>
    },
    {
      path : '/pastes',
      element:
      <div>
        <Navbar></Navbar>
        <Pastes></Pastes>
      </div>
    },
    {
      path : '/pastes/:id',
      element:
      <div>
        <Navbar></Navbar>
        <ViewPaste></ViewPaste>
      </div>
    }
  ]
)

function App() {

  return (
    <div>
        <RouterProvider router= {router}>

        </RouterProvider>
    </div>
  )
}

export default App
