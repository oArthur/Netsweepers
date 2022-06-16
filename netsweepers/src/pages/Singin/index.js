import React from 'react';
import { KeyboardView, Title, Desc, Container, Input, ButtonSubmit, TextSubmit, Label, Line, ForgotPass, RememberMe } from './styles';
import Header from '../../components/Header';

function Singin() {
    return (
        <KeyboardView
            behavior={Platform.OS === 'ios' ? "padding" : "height"}>
            <Header />
            <Title>Log in</Title>
            <Desc>Welcolme to netweepers portal. Please put your login credentials bellow to start using the app. Not a client yet? Click Here</Desc>
            <Container>
                <Label>User / E-mail</Label>
                <Input
                    placeholderTextColor="rgba(0, 0, 0, 0.4)"
                    placeholder="exemple@dominio.com" />
                <Label>Password</Label>
                <Input
                    placeholderTextColor="rgba(0, 0, 0, 0.4)"
                    placeholder="Password"
                    secureTextEntry />
                <ForgotPass>Forgot password?</ForgotPass>
                <Line></Line>
                <RememberMe>✓ Remember me</RememberMe>
                <ButtonSubmit>
                    <TextSubmit>Log in</TextSubmit>
                </ButtonSubmit>


            </Container>
        </KeyboardView>

    )
}

export default Singin;