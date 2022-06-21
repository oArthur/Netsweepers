import styled from 'styled-components/native';

export const KeyboardView = styled.KeyboardAvoidingView`
    flex: 1;
    align-items: center;
    justify-content: center;
    background-color: #022873;
`
export const Container = styled.View`
    flex: 1;
    justify-content: flex-start;
    align-items: center;
    padding-bottom: 30px;
    padding-top: 20px;
    background-color: #fff;
    border-radius: 20px;
    width: 100%;
    max-height: 65%;
    min-height: 60%;
    `       

export const Title = styled.Text`
    color: white;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 15px;
    align-self: flex-start;
    margin-left: 5%;    
`
export const Desc = styled.Text`
    color: rgba(255, 255, 255, 0.7);
    font-size: 14px;
    align-self: flex-start;
    margin-left: 5%;
    margin-bottom: 10px;

`
//font-family: 'Poppins';
export const Input = styled.TextInput`
    border: 2px solid #000
    padding: 12px 20px;
    color: #000;
    font-size: 20px;
    border-radius: 9px;
    width: 90%;
    height: 50px;

`

export const Label = styled.Text`
    color: #000;
    font-size: 16px;
    font-weight: bold;
    align-self: flex-start;
    margin-left: 6%;
    padding: 12px;
`
export const ButtonSubmit = styled.TouchableOpacity`
    background-color: #022873;
    border-radius: 9px;
    width: 70%;
    padding: 15px 20px;
`

export const TextSubmit = styled.Text`
    color: #fff;
    text-align: center;
    font-size: 16px;
    font-weight: bold;

`

export const Line = styled.View`
    border-bottom-color: black;
    border-bottom-width: 15px;
`
export const ForgotPass = styled.Text`
    color: #BF0404;
    font-weight: bold;
    align-self: flex-end;
    margin-right: 6%; 
    padding: 10px;
`
export const RememberMe = styled.Text`
    color: rgba(0, 0, 0, 0.8);
    align-self: flex-start;
    margin-left: 6%; 
    padding: 10px;

`