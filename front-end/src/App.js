import React,{useState, useEffect} from 'react'
import axios from 'axios'
import NavBar from './GenrealWebPage/NavBar'
import { BrowserRouter , Route , Routes } from 'react-router-dom'
import Home from './GenrealWebPage/Home'
import EletronicsPage from './GenrealWebPage/EletronicsPage'
import './App.css';

// function App() {
//     const [data,setData] = useState (null)
//     useEffect (() =>
//     {
//         axios.get("/members").then(
//             res => res.data
//         ).then(
//             data => data.members
//         ).then(
//             members => setData(members)
//         )

//     },[])
//     console.log(data)
//   return (
//     <div>{(data=== null) ? (<p>Loading....</p>) : ( data.map((member,i) =>(
//         <p key={i}>{member}</p>
//     )))}</div>
//   )
// }
const App = () =>{

    return (
        <div>
        <BrowserRouter>
            <div>
                <NavBar/>
                <Routes>
                    <Route path = '/' element={<Home/>}/>
                    <Route path = '/Tech' element = {<EletronicsPage/>} />
                </Routes>

            </div>
        </BrowserRouter>
        </div>
    )
}

export default App