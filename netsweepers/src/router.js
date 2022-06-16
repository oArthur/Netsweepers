import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack'

import Home from './pages/Home';
import Detail from './pages/Detail';
import Singin from './pages/Singin';
const Stack = createNativeStackNavigator();

function Routes(){
    return(
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen name="Home" component={Home} options={{ headerShown: false }} />
                <Stack.Screen name="Singin" component={Singin} options={{ headerShown: false }}/>
                <Stack.Screen name="Detail" component={Detail} />
            </Stack.Navigator> 
        </NavigationContainer>
    );
}
export default Routes;