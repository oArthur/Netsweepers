import React from 'react';
import { Card, Title, Num, Image } from './style';
import { StyleSheet } from 'react-native';


function CardsItem(props) {
  const styles = StyleSheet.create({
    cardColor: {
      backgroundColor: props.color || '#fff',
    },
    titleColor: {
      color: props.tcolor || '#000',
    },
    titleFont:{
      marginBottom: props.bottom || 0,
    }
  });
  return (
    <Card style={styles.cardColor}>
      <Title style={[styles.titleColor, styles.titleFont]}>{props.title}</Title>
      <Num>{props.num}</Num>
      <Image source={props.img} resizeMode="cover" />
    </Card>
  );
}

export default CardsItem;
