import React from 'react';
import { MaterialIcons } from '@expo/vector-icons';
import { Container, Title, Back, Label, User, ContainerCard, Card, HeaderBottom, ItemHeader, Link, ItemSelected, Image } from './style';

import CardsItem from '../../components/CardDash';
import { useNavigation } from '@react-navigation/native';

 
const img1 = { uri: "https://i.imgur.com/8H72S4P.png" };
const img2 = { uri: "https://i.imgur.com/6OXCmyQ.png" };
const img3 = { uri: "https://i.imgur.com/qTQ6pk8.png" };

export default function Dashboard() {
    const navigation = useNavigation();

 return (
    <Container>
        <Back onPress={() => navigation.navigate("Home")}><MaterialIcons name="arrow-back" size={28} color="#fff"/></Back>
        <Label>Overview</Label>
        <Title>Dashboard</Title>
        <User><MaterialIcons name="account-circle" size={45} color="#fff" /></User>
        <CardsItem img={img1} title="Positivas" num="65%" color="#1C7B0D" ></CardsItem>
        <CardsItem img={img2} title="Negativas" num="35%" color="#D00D0D"></CardsItem>
        <CardsItem img={img3} title="Palavras Mais Citadas" bottom={7} color="#000" tcolor="#fff"></CardsItem>
        
    </Container>
    
  );
}
{/* <HeaderBottom>
            <Link><ItemHeader>Day</ItemHeader></Link>
            <Link><ItemHeader>Week</ItemHeader></Link>
            <Link><ItemSelected>Month</ItemSelected></Link>
            <Link><ItemHeader>Year</ItemHeader></Link>
        </HeaderBottom> */}