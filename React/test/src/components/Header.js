import React from 'react'

// rfc
export default function Header() {
  return (
    <header>
        <div>
            <span className='logo'>House staff</span>
            <ul className='nav'>
                <li>Про нас</li>
                <li>Контакты</li>
                <li>Кабинет</li>
            </ul>
        </div>
        <div className='presentation'></div>
    </header>
  )
}
