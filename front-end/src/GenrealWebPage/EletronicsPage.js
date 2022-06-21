import React from 'react'
import axios from 'axios'
import { useState } from 'react'
const EletronicsPage = () => {
    const [isOn,setIsOn] = useState(true)
    function setBulb(){
        if(isOn===true){
            setIsOn(false)
            axios.get("/lightBulbOff")
        }
        else
        {            
            setIsOn(true)
            axios.get("/lightBulbOn")

        }
    }
    function setColorBulb(color){
        if(color == "Blue"){
            axios.get("/lightBulbBlue")
        }
        if(color==="Red"){
            axios.get("/lightBulbRed")
        }
        if(color==="Green"){
            axios.get("/lightBulbGreen")
        }
    }
    function getIsOn(){
        axios.get("/isOn").then(
            res =>{
                console.log("Look at me.")
                console.log(res)
                 return res }
        )
    }
    return (
    <div> 
        <h1>This is the EletronicsPage</h1>
        <button onClick={ () =>setBulb()}>{isOn ? ("Off"):("On")}</button>
        <button onClick={ () =>setColorBulb("Blue")}>Blue</button>
        <button onClick={() =>setColorBulb("Red")}>Red</button>
        <button onClick={() =>setColorBulb("Green")}>Green</button>
        <button onClick={() => getIsOn()}>Test</button>
        
        {/* <p>{() => getIsOn()} hello </p> */}


    </div>
  )
}

export default EletronicsPage