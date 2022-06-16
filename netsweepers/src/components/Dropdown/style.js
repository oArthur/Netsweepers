import React from 'react';

import { StyleSheet } from 'react-native';

export const Styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#022873',
        border: '1px solid #fff',
        borderRadius: 10,
    },
    dropdown1RowStyle: {
        backgroundColor: 'rgba(255, 255, 255, 0.9);',
        borderBottomColor: 'rgba(255, 255, 255, 0.9);'
    },
    dropdown1BtnTxtStyle: {
        color: '#fff', 
        textAlign: 'center',
        fontSize: 18,
        fontWeight: 'bold',
    },
    dropdown1DropdownStyle: {
        backgroundColor: 'rgba(0, 0, 0, 0.4);'
    },
    dropdown1RowTxtStyle: {
        color: '#022873' , textAlign: 'left'
    },
    dropdown1BtnStyle: {
        backgroundColor: 'rgba(255, 255, 255, 0);',
        borderRadius: 4,
        borderWidth: 1,
        borderColor: '#rgba(255, 255, 255, 0.6);',
        width: '90%',
      },
})