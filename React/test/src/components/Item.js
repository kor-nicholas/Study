import React, { Component } from 'react'

// Так как тут уже все показывается пользователю, то мы как буд-то находимся в папке public и от туда достаем фото
export class Item extends Component {
    render() {
        return (
            <div className='item'>
                <img src={'./img/' + this.props.item.img}/>
                <h2>{this.props.item.title}</h2>
                <p>{this.props.item.desc}</p>
                <b>{this.props.item.price}$</b>
                <div className='add-to-cart'>+</div>
            </div>
        )
    }
}

export default Item