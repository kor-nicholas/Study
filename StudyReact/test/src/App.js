import React from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Items from "./components/Items";

class App extends React.Component {

  /* состояния - "база товаров" */
  constructor(props){
    super(props) /* передача родителю */
    this.state = {
      items: [
        {
          id: 1,
          title: 'Title',
          img: 'doska_s_uporami_dlya_otzhimaniya_raznym_hvatom_1.jpg',
          desc: 'Desc',
          category: 'Category',
          price: 'Price'
        },
        {
          id: 2,
          title: 'Бюстгалтер Puma Women T-Shirt Bra 1P Black 80B',
          img: '907508_01.jpg',
          desc: 'Характеристики и изображения товара Бюстгалтер Puma Women T-Shirt Bra 1P Black 80B приведены в ознакомительных целях и могут отличаться от реальных. Рекомендуем при покупке уточнять наличие желаемых функций и характеристик.',
          category: 'бра ',
          price: '699'
        },
        {
          id: 3,
          title: 'Піжама Police',
          img: '23-1.jpg',
          desc: 'Абсолютний хіт продажів бренду – жіноча піжама із “Шовку Армані”. Спокусливий коротенький топ, із високоякісним принтом, підкреслить сексуальність, а міні-шорти не будуть сковувати рухів. Саме таким повинен бути ідеальний одяг для дому: комфортним і привабливим. Піжама з легкої та дихаючої тканини від Swatti може стати вашою улюбленою піжамою або домашнім образом. Вона підкреслить ваш силует і сяде по фігурі завдяки можливості регулюванні довжини бретельок. Порадуйте себе, вибирайте те, що зручно і сучасно. Жіноча піжама – це не тільки наряд для сну, переконайтеся самі.',
          category: 'Головна/Короткі піжами/Піжама Police',
          price: '749,00 ₴'
        },
        {
          id: 4,
          title: 'Carrello Sigma 2в1 (CRL-6509), универсальная коляска',
          img: '4180.jpg',
          desc: 'Наружный текстиль  всех модулей коляски обладает высокой степенью защиты от влаги и ультрафиолета (SPF-50)',
          category: 'Главная » Универсальные коляски',
          price: '14400'
        },
        {
          id: 5,
          title: 'Forcado Pull Reducer, Waist Reducer Body Shaper Trimmer for Reducing Your Waistline and Burn Off Extra Calories, Arm Exercise, Tummy Fat Burner, Body Building Training, Toning Tube (Multicolor)',
          img: 'tyagovyy-trenazher-rower-2.jpg',
          desc: 'I purchased this product because i didnt get time for gym.. This product is durable, strength. Attractive in color and it made up from durable soft material.. Will be one of the best collections for home workout..',
          category: 'Sports, Fitness & Outdoors›Exercise & Fitness›Strength Training Equipment',
          price: 'Currently unavailable'
        },
        {
          id: 6,
          title: 'Shapewear for Women Tummy Control Full Body Shaper Plus Size Fajas Colombianas Post Surgery Compression Garment',
          img: 'cami-hot-hot-shapers_1-400x400-product_thumb.jpg',
          desc: '👗 3 LAYERS OF FABRIC / FIRM COMPRESSION: Speed up recovery after giving birth or after your surgery with our fajas post surgery compression garment. Firm abdominal control to prevent water retention and strong 3 layer fabric for maximum support and shaping. (Especially the middle layer with rubber design provides compression for the abdomen, helps to flatten your tummy and feel comfy and safe with our colombian fajas for women. )',
          category: 'Home / Clothing, Shoes & Jewelry / Women / Clothing / Lingerie, Sleep & Lounge / Lingerie / Shapewear / Bodysuits / Shapewear for Women Tummy Control Full Body...',
          price: 'INR5686'
        },
        {
          id: 7,
          title: 'Литовские железные дороги будут перевозить посылки из Китая',
          img: 'images.jfif',
          desc: 'Находящаяся в госуправлении литовская железнодорожная компания Lietuvos gelezinkeliai в этом году впервые будет провозить по территории страны почтовые посылки, поставляемые из Китая в Литву. Первый пробный груз планируется в мае.',
          category: 'news',
          price: '1463'
        }
      ]
    }
  }
  
  /* передаем массив с товарами из состояния (items - товары) */
  render() {
    return (
      <div className="wrapper">
        <Header />
        <Items items={this.state.items} />
        <Footer />
      </div>
    )
  }
}

export default App;
