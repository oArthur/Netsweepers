import styled from 'styled-components/native';

export const Container = styled.View`
    flex: 1;
    background-color: #022873;
    width: 100%;
    height: 100%;
`
export const Back = styled.TouchableOpacity`
margin-top: 12%;
color: #fff;
margin-left: 1%;
margin-bottom: 5%;
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
    margin-left: 5%;    
`
export const Label = styled.Text`
    color: rgba(255, 255, 255, 0.7);
    font-size: 15px;
    font-weight: bold;
    align-self: flex-start;
    margin-left: 6%;    
`
export const HeaderBottom = styled.View`
    flex: 1;
    width: 100%;
    max-height: 10%;
    flex-direction: row;
    justify-content: space-between;
    align-items: start;
    background-color: #fff;
    padding: 15px;
    border-radius: 9px;
    top: 35%;
    
`
export const Link = styled.TouchableOpacity`

`
export const ItemHeader = styled.Text`
    color : #000;
    font-size: 16px;
    font-weight: bold;
`
export const ItemSelected = styled.Text`
    color : #1D8CF2;
    font-size: 17px;
    text-decoration: underline #1D8CF2;
    font-weight: bold;
`
export const Image = styled.Image`
    flex: 1;
`
