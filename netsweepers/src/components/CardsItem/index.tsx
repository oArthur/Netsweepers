import React from 'react';
import { Card, CardTitle, CardNum, CardTextLink } from './styles';
import { MaterialIcons } from '@expo/vector-icons';
import { CardComp } from '../../Data/data';
 

export default function CardsItem({title, number} : CardComp) {

    function convertNumber(number) {
        return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    }

 return (
   <Card>
    <CardTitle>{title}</CardTitle>
    <CardNum>{convertNumber(number)}</CardNum>
    <MaterialIcons name="bar-chart" size={45} color="#000" />
    <CardTextLink>Ver ➤</CardTextLink>
    </Card>
  );
}
