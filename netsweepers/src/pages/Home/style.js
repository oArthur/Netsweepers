import styled from 'styled-components/native';

export const Container = styled.View`
    flex: 1;
    background-color: #022873;
`
export const Hambuguer = styled.TouchableOpacity`
    margin-top: 15%;
    color: #fff;
    margin-left: 5%;
    margin-bottom: 10%;
    postion: absolute;
`
export const User = styled.TouchableOpacity`
    margin-right: 5%;
    align-self: flex-end
    postion: absolute;
    bottom: 40px;
`

export const Title = styled.Text`
    color: white;
    font-size: 30px;
    font-weight: bold;
    align-self: flex-start;
    margin-left: 8%;    
`
export const TitleNum = styled.Text`
    color: white;
    font-size: 38px;
    font-weight: bold;
    padding-top: 10px;
    align-self: flex-start;
    margin-left: 8%;    
`
export const Label = styled.Text`
    color: rgba(255, 255, 255, 0.7);
    font-size: 15px;
    font-weight: bold;
    align-self: flex-start;
    margin-left: 8%;    
`

export const CardsContainer = styled.FlatList`
    width: 100%;
    margin-top: 25%;
    margin-bottom: 30px;
`
export const TitleBottom = styled.Text`
    color: white;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
    text-decoration: underline #fff;
`
export const Link = styled.TouchableOpacity`
    align-itens: center;
    justify-content: center;
    margin-bottom: 10%;
`

