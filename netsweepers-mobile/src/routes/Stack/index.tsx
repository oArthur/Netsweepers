import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack'


import Home from '../../pages/Home';
import Singin from '../../pages/Singin';
import Dashboard from '../../pages/Dashboard';
import { propsNavigationStack } from '../Models';

const { Navigator, Screen }  = createNativeStackNavigator<propsNavigationStack>();

export default function(){
    return(
        <Navigator initialRouteName='Singin'>
            <Screen name="Singin" component={Singin} options={{ headerShown: false }}/>
            <Screen name="Home" component={Home} options={{ headerShown: false }} />
            <Screen name="Dashboard" component={Dashboard} options={{ headerShown: false }} />
        </Navigator>
    );
}