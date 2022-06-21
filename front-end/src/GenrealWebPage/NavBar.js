import React from 'react'
import {Link } from 'react-router-dom'

const NavBar = () =>{
    return(
        <nav className="NavBarCSS">
            <div className="container">
                <a className="brand-logo">Poke' Times</a>
                <ul className='right'>
                    <li><Link to={"/"} href="/"><button>Home</button></Link></li>
                    <li><button><Link to={"/Tech"}>Tech</Link></button></li>
                </ul>
            </div>
        </nav>
    )
}

export default NavBar;