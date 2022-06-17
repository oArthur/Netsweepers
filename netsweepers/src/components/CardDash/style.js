import styled from 'styled-components/native';

export const Card = styled.TouchableOpacity`
    background-color: #fff;
    border-radius: 9px;
    margin-top: 5%;
    width: 90%;
    height: 130px;
    padding: 15px;
    justify-content: space-between;
    margin-left: 20px;
`
export const Title = styled.Text`
    color: #000;
    font-size: 16px;
    font-weight: bold;
`
export const Num = styled.Text`
    color: #000;
    font-size: 16px;
    font-weight: bold;
    text-align: right;
    z-index: 1;
    bottom: 22px;
    
`
export const Image = styled.ImageBackground`
    width: 100%;
    height: 91px;
    bottom: 20px;
`