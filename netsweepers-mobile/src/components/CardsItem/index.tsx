import React from 'react';
import { Card, CardTitle, CardNum, CardTextLink } from './styles';
import { MaterialIcons } from '@expo/vector-icons';
import { CardComp, convertNumber } from '../../Data/data';
 

export default function CardsItem({title, number} : CardComp) {
 return (
   <Card>
    <CardTitle>{title}</CardTitle>
    <CardNum>{convertNumber(number)}</CardNum>
    <MaterialIcons name="bar-chart" size={45} color="#000" />
    <CardTextLink>Ver ➤</CardTextLink>
    </Card>
  );
}
