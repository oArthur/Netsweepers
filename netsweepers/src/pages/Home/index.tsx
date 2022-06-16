import React from 'react';
import { MaterialIcons } from '@expo/vector-icons';
import { Container, Hambuguer, Title,TitleNum, Label, User, CardsContainer, TitleBottom, Link, ViewDropdown } from './style'

import CardsItem  from "../../components/CardsItem";
import { ListRenderItemInfo } from 'react-native';
import { CardComp, CardList, SomaLista, convertNumber } from '../../Data/data';
import { SeparatorItem } from '../../components/SeparadorItem/SeparadorItem';

import Dropdown from '../../components/Dropdown';

export default function Home() {
  function renderItem({item}: ListRenderItemInfo<CardComp>) {
    return<CardsItem{...item}/> 
  }
  console.log(SomaLista())

  
  return (
    <Container>  
      <Hambuguer>
        <MaterialIcons
          name="list"
          size={30}
          color="#fff" /></Hambuguer>
      <Title>Olá, Netsweepers</Title>
      <User>
      <MaterialIcons
          name="account-circle"
          size={45}
          color="#fff" />
      </User>
      <Label>Total de menções</Label>
      <TitleNum>{convertNumber(SomaLista())}</TitleNum>
      <ViewDropdown><Dropdown /></ViewDropdown> 
      <CardsContainer
      horizontal 
      ItemSeparadorComponent={SeparatorItem}
      data={CardList}
      keyExtractor={(item) => item.title}
      renderItem={renderItem}
      />
      <Link><TitleBottom>My Dashboard ➤ </TitleBottom></Link>
    </Container>
  );
}