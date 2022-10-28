import React from 'react'
import Switch from '../Switch/Switch'

export default function Home() {
  return (
    <div className='mt-14 ml-[5%] mr-[5%]'>
        <h2 className='text-brand font-bold text-[34px]'>Informações básicas</h2>
        <div className='border-[1px] mt-11'></div>

        <form className='flex justify-evenly'>
            <div className='w-full'>
                <label className='mt-14'>
                    Cidade
                    <input type="text" />
                </label>
                <label className='mt-14'>
                    Quantidade de quartos
                    <input type="number" />
                </label>
                <label className='mt-14'>
                    Vagas de garagem
                    <input type="number" />
                </label>
                <label className='mt-14'>
                    Qual o seu andar favorito
                    <input type="number" />
                </label>
            </div>
            <div className='w-full'>
            <label className='mt-14'>
                Cidade
                <input type="text" />
            </label>
            <label className='mt-14'>
                Quantidade de quartos
                <input type="number" />
            </label>
            <label className='mt-14'>
                Vagas de garagem
                <Switch/>
            </label>
            <label className='mt-14'>
                Qual o seu andar favorito
                <input type="number" />
            </label>
            </div>
           
        </form>
    </div>
  )
}
